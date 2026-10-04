import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

def calldata_compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out

contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1];ENV=(ROOT.parents[3]/'accounts.env').read_text();ADDRESS=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
def account(number):return create_account(account_private_key=re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip())
def client(number):return create_client(chain=studionet,account=account(number))
def write(number,name,args):
 c=client(number);tx=c.write_contract(address=ADDRESS,function_name=name,args=args);print(name+'_tx='+str(tx),flush=True);receipt=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True);leader=(receipt.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert receipt.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS';return str(tx)
notice_id='NOTICE-'+str(int(time.time()));publication='https://raw.githubusercontent.com/warnedwarn/notice-clock/main/docs/evidence/publication.md';effective='https://cdn.jsdelivr.net/gh/warnedwarn/notice-clock@main/docs/evidence/effective-date.md';transactions={'post':write(2,'post_notice',[notice_id,'Harbor evening entry procedure',publication,effective,30]),'measure':write(3,'measure_notice',[notice_id])};state=client(2).read_contract(address=ADDRESS,function_name='get_notice',args=[notice_id]);assert state['state']=='TIMELY' and int(state['gap_days'])==44;proof={'noticeId':notice_id,'transactions':transactions,'state':state,'fixtureDisclosure':'Wallets and evidence pages are operator-controlled fixtures.'};(ROOT/'evidence').mkdir(exist_ok=True);(ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2),flush=True)
