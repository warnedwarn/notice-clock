from pathlib import Path
HTML = (Path(__file__).parents[1] / 'docs' / 'index.html').read_text()
def test_browser_controls():
 for item in ('id="connect"','id="post"','id="measure"','id="revise"','id="load"','id="demo"','FINALIZED','get_notice'): assert item in HTML
def test_calendar_identity():
 assert 'class="tearoff"' in HTML and 'PUBLICATION DAY' in HTML and 'LEAD-TIME RULER' in HTML
