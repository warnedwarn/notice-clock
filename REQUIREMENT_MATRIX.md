# Verification ledger

| Gate | Evidence | Status |
|---|---|---|
| Stronger source authority | Governor registry plus origin and path-prefix binding for both distinct source slots | PASS source + live |
| Trust-sensitive consequence | Deterministic gap policy issues `AUTHORIZED` or `DENIED`; only the beneficiary can consume once | PASS source + live |
| Exact source-bound dates | Validator principle binds exact dates, conflict indexes, and ordered digests | PASS tests |
| Permissionless measurement and safe revision | Measurement has no caller restriction; conflict revision is owner-only and remains authority-bound | PASS tests |
| StudioNet deployment and source match | New deployment manifest and fetched-source digest | PASS |
| Complete live lifecycle | approve authorities, post, measure, consume, and final readback | PASS (`NOTICE-1791257206`) |
| Canonical browser run | public site uses corrected address, exposes the complete flow, and has no console errors | PASS |
