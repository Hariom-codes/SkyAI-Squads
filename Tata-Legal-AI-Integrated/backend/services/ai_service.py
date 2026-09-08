import json, os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from google import genai
load_dotenv(); GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY: raise ValueError('GEMINI_API_KEY is not set in the .env file')
client=genai.Client(api_key=GEMINI_API_KEY); MODEL_NAME=os.getenv('GEMINI_MODEL','gemini-3.5-flash-lite')
def _json_response(prompt,fallback):
    try:
        r=client.models.generate_content(model=MODEL_NAME,contents=prompt,config={'temperature':0,'max_output_tokens':1200,'response_mime_type':'application/json'})
        return json.loads((r.text or '').strip())
    except Exception as e:
        x=dict(fallback); x['error']=str(e); return x
def _normalize(a,clause_name):
    if not isinstance(a,dict): a={}
    a.setdefault('clause_name',clause_name); a.setdefault('summary','AI analysis could not be completed.'); a.setdefault('risk_level','Unknown'); a.setdefault('risk_reason',''); a.setdefault('recommendation','Please review this clause manually.')
    try:a['confidence']=max(0,min(100,int(a.get('confidence',0))))
    except:a['confidence']=0
    return a
def analyze_clause(clause_name,clause_text,retrieved_context=''):
    prompt=f'''You are a legal contract analysis assistant. Analyze this clause using its text and retrieved project knowledge. Do not invent facts. Identify practical legal risk, explain why, and give a practical recommendation. Return ONLY valid JSON.\nClause name: {clause_name}\nClause text: {clause_text[:5000]}\nRelevant knowledge:\n{retrieved_context[:5000]}\nReturn exactly: {{"clause_name":"...","summary":"...","risk_level":"Low | Medium | High","confidence":0,"risk_reason":"...","recommendation":"..."}}'''
    return _normalize(_json_response(prompt,{}),clause_name)
def _analyze_batch(batch):
    payload=[{'index':i,'clause_name':x['clause_name'],'clause_text':x['clause_text'][:4000],'knowledge':x['knowledge'][:3500]} for i,x in enumerate(batch)]
    prompt=f'''You are a legal contract analysis assistant. Analyze every clause independently. Use only supplied facts and knowledge. Return ONLY a JSON array with exactly one object per input item, preserving index. Each object: index, clause_name, summary, risk_level (Low/Medium/High), confidence (0-100 integer), risk_reason, recommendation. INPUT: {json.dumps(payload,ensure_ascii=False)}'''
    try:
        r=client.models.generate_content(model=MODEL_NAME,contents=prompt,config={'temperature':0,'max_output_tokens':min(7000,max(2200,1100*len(batch))),'response_mime_type':'application/json'})
        data=json.loads((r.text or '').strip()); return data if isinstance(data,list) else []
    except Exception:return []
def analyze_clauses_fast(items,batch_size=6):
    if not items:return []
    batches=[items[i:i+batch_size] for i in range(0,len(items),batch_size)]; slots=[None]*len(batches)
    with ThreadPoolExecutor(max_workers=min(4,len(batches))) as ex:
        fs={ex.submit(_analyze_batch,b):i for i,b in enumerate(batches)}
        for f in as_completed(fs): slots[fs[f]]=f.result()
    out=[]
    for bi,batch in enumerate(batches):
        by={int(x.get('index')):x for x in (slots[bi] or []) if isinstance(x,dict) and str(x.get('index','')).isdigit()}
        for i,item in enumerate(batch):
            a=by.get(i) or analyze_clause(item['clause_name'],item['clause_text'],item['knowledge']); a.pop('index',None); out.append(_normalize(a,item['clause_name']))
    return out
def summarize_document(clauses):
    compact=[{'clause_name':c.get('clause_name'),'risk_level':c.get('analysis',{}).get('risk_level','Unknown'),'summary':c.get('analysis',{}).get('summary',''),'recommendation':c.get('analysis',{}).get('recommendation','')} for c in clauses]
    prompt=f'''Create a concise executive summary from these clause analyses. Do not invent facts. Return ONLY valid JSON: {{"summary":"2-5 sentence executive summary","overall_risk":"Low | Medium | High | Unknown"}}\n{json.dumps(compact,ensure_ascii=False)}'''
    return _json_response(prompt,{'summary':'A document-level summary could not be generated. Review the clause analyses below.','overall_risk':'Unknown'})
