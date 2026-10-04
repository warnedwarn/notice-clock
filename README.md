# Notice Clock

## Read the interval, not the announcement

A publication date and an effective date are facts from two different records. Notice Clock asks validators to retrieve both records and agree on the exact ISO dates. Contract code then measures the calendar gap and decides whether the configured minimum lead time was met.

```text
PUBLICATION  2026-09-01
                 | 44 calendar days
EFFECTIVE    2026-10-15
MINIMUM      30 days
RESULT       TIMELY
```

## Clock states

`OPEN` can be measured by any caller. Exact dates produce `TIMELY` or `LATE`. Missing or contradictory dates produce `CONFLICT`. A conflicted notice exposes one owner-only source replacement, moves through `REVISED`, and can then be measured permissionlessly again. The original notice ID, minimum lead time, ownership, source digests, and revision flag remain inspectable.

## Guardrails

The two records must use distinct parsed HTTPS origins. Dates are bounded to valid calendar values from 1970 through 2200. The model never decides whether notice is timely: it only extracts dates or explicit conflict indexes. Deterministic code performs the day arithmetic.

## Test the clock

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

Sample records and demo wallets are operator-controlled fixtures, not authenticated government notices.

## Published measurement station

The public station is live at https://notice-clock.pages.dev/ and its source is at https://github.com/warnedwarn/notice-clock. The StudioNet contract is `0xEaB42219B0707Aa42a8E76254E833A447aB1DD8E`. Its interface uses source tickets, a circular day dial, a physical measurement lever, and a human-readable result stamp—there is no generic JSON receipt panel.

Two independent runs now agree on the same calendar result. The scripted record `NOTICE-1791084136` and the canonical browser record `NOTICE-1791085029056` both resolved to `TIMELY` with a 44-day interval. Receipts, digests, and transaction hashes are preserved in `evidence/` rather than folded into this clock-face overview.
