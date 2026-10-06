# Verification ledger

| Gate | Evidence | Status |
|---|---|---|
| Stronger source authority | Governor registry plus origin and path-prefix binding for both distinct source slots | PASS source, deployment pending |
| Trust-sensitive consequence | Deterministic gap policy issues `AUTHORIZED` or `DENIED`; only the beneficiary can consume once | PASS source, deployment pending |
| Exact source-bound dates | Validator principle binds exact dates, conflict indexes, and ordered digests | PASS tests |
| Permissionless measurement and safe revision | Measurement has no caller restriction; conflict revision is owner-only and remains authority-bound | PASS tests |
| StudioNet deployment and source match | New deployment manifest and fetched-source digest | UNVERIFIED |
| Complete live lifecycle | approve authorities, post, measure, consume, and final readback | UNVERIFIED |
| Canonical browser run | public site uses corrected address and reaches consumed authorization | UNVERIFIED |
