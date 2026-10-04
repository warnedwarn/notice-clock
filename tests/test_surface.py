from pathlib import Path
HTML = (Path(__file__).parents[1] / 'docs' / 'index.html').read_text()
def test_browser_controls():
 for item in ('id="connect"','id="post"','id="measure"','id="revise"','id="load"','id="demo"','FINALIZED','get_notice'): assert item in HTML
 assert 'c||createClient({chain:studionet,endpoint:ENDPOINT})' in HTML
def test_calendar_identity():
 assert 'class="date-dial"' in HTML and 'class="progress-stations"' in HTML
 assert 'DATES ENTER.' in HTML.upper() and 'READ THE STAMP' in HTML
 assert '<pre' not in HTML and 'class="receipt"' not in HTML
