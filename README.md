# Notice Clock

## Read the interval, not the announcement

A publication date and an effective date are facts from two approved authority records. Notice Clock asks validators to retrieve both records and agree on the exact ISO dates. Contract code measures the calendar gap, issues `AUTHORIZED` or `DENIED`, and lets only the named beneficiary consume an authorization once.

```text
PUBLICATION  2026-09-01
                 | 44 calendar days
EFFECTIVE    2026-10-15
MINIMUM      30 days
RESULT       TIMELY
```

## Clock states

`OPEN` can be measured by any caller. Exact dates move the record to `VERIFIED` with an `AUTHORIZED` or `DENIED` decision. Missing or contradictory dates produce `CONFLICT`. A conflicted notice exposes one owner-only, authority-bound source replacement and can then be measured permissionlessly again. An authorized decision becomes `CONSUMED` only when the named beneficiary invokes the frozen consequence.

## Guardrails

Only the deployment governor can register a source authority. Every evidence URL must match that authority's normalized HTTPS origin and directory prefix, and the publication and effective-date slots must use distinct approved authorities. Dates are bounded to valid calendar values from 1970 through 2200. The model only extracts dates or conflict indexes. Deterministic code performs the day arithmetic and controls the consequence.

## Test the clock

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

Sample authorities, records, and demo wallets are operator-controlled fixtures used to prove the trust boundary. They are not represented as independent government publishers.

## Published measurement station

The public station is live at https://notice-clock.pages.dev/ and its source is at https://github.com/warnedwarn/notice-clock. The corrected StudioNet contract is `0x7aB5599F4E80DD61781D14252d73D04Bf7E8Bdbe`. Its interface uses source tickets, a circular day dial, a physical measurement lever, and a human-readable result stamp—there is no generic JSON receipt panel.

The corrected lifecycle record `NOTICE-1791257206` resolved to `AUTHORIZED`, measured a 44-day interval, and was consumed exactly once by its named beneficiary. Receipts, ordered source digests, and every transaction hash are preserved in `evidence/` rather than folded into this station overview.
