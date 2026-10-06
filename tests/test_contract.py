import ast
from pathlib import Path

SOURCE = (Path(__file__).parents[1] / 'contracts' / 'contract.py').read_text(); TREE = ast.parse(SOURCE)
def load(name):
 node = next(item for item in TREE.body if isinstance(item, ast.FunctionDef) and item.name == name); scope = {}
 exec(compile(ast.Module(body=[node], type_ignores=[]), '<contract>', 'exec'), scope); return scope[name]

def test_date_math():
 leap = load('leap'); scope = {'leap':leap,'clean':lambda v,n=10:str(v).strip()[:n]}; node = next(item for item in TREE.body if isinstance(item, ast.FunctionDef) and item.name == 'parse_date'); exec(compile(ast.Module(body=[node],type_ignores=[]),'<contract>','exec'),scope); parse = scope['parse_date']
 assert parse('2026-10-15')[1] - parse('2026-09-01')[1] == 44

def test_complete_surface():
 for name in ('approve_authority','post_notice','measure_notice','consume_release','revise_source','get_authority','get_notice'): assert f'def {name}' in SOURCE

def test_consensus_binds_dates_conflicts_and_digests():
 assert 'both exact ISO dates, every conflict index, and both ordered full-response digests must match' in SOURCE

def test_revision_is_owner_only_and_once():
 assert "notice.state != 'CONFLICT'" in SOURCE and 'notice.revised' in SOURCE
 assert "address(gl.message.sender_address) != address(notice.owner)" in SOURCE

def test_permissionless_measure_and_distinct_sources():
 section = SOURCE[SOURCE.index('def measure_notice'):SOURCE.index('def consume_release')]
 assert 'sender_address' not in section
 assert 'pub_origin == eff_origin' in SOURCE

def test_authority_registry_binds_both_source_slots():
 assert "governor authority required" in SOURCE
 assert "source must match its approved authority" in SOURCE
 assert "pub_id == eff_id" in SOURCE and "publication_authority" in SOURCE and "effective_authority" in SOURCE

def test_verified_interval_gates_a_single_beneficiary_release():
 assert "notice.decision = 'AUTHORIZED' if gap >= int(notice.minimum_days) else 'DENIED'" in SOURCE
 consume = SOURCE[SOURCE.index('def consume_release'):SOURCE.index('def revise_source')]
 assert "beneficiary required" in consume and "notice.state != 'VERIFIED'" in consume
 assert "notice.state = 'CONSUMED'" in consume
