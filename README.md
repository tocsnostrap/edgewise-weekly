# Edgewise weekly: Bitcoin's week, frozen on Monday, checked on Saturday

Every Monday, Edgewise publishes how Bitcoin's week could play out. Every Saturday, it checks that against what
actually happened. This repository holds the Monday reads, frozen before the week plays out, so anyone can check that
nothing was changed afterwards.

## What gets frozen each Monday (UTC)

- **00:05**: Bitcoin's week band, as the Edgewise app shows it at the week's open. It is the middle 20 / 40 / 60 / 80%
  of where Bitcoin's last 104 weeks closed, measured from the open, at every hour of the week.
  We tested this weekly range, set at Monday's open, on almost 5 years of past Bitcoin weeks. Bitcoin finished the week
  inside it about 5 weeks in 6. So about 1 week in 6 it ends outside, and that can happen two weeks in a row.
  (R&D's registered wording since 14 Oct 2026; the measured figure is 83.1% over 248 weeks.)
- **08:05**: the app's closest matching week (its "% similar" score and its candles plotted forward). This is one past
  week, not a forecast. "Similar" means the week's first hours moved like this week's. It is never scored as a
  prediction; Saturday simply shows how far it finished from the real week.

Each file's SHA-256 is listed in `frozen/SHA256SUMS`, and the commit time on GitHub shows when it was published.

## What gets checked

- **Saturday:** Bitcoin's price at Friday's close, against the frozen band at Friday's close. Bitcoin keeps
  trading through the weekend, so this is labelled "at Friday's close" and is not the week's result.
- **Monday:** the week's own close (Sunday 24:00 UTC), against the frozen band.

`rehearsal/` holds pipeline tests computed **after** their week. They are never a freeze and never scored. The record in `frozen/`
starts with the week of 12 Oct 2026.

Nothing is re-scored or back-filled. A week whose freeze missed its deadline is not scored, and says so.

edgewise.to

## Weekly pick (from 2026-10-12)

Each Monday at 10:00 UTC we take the app's top closest-match week as that week's pick and post it. The scored pick is `picks/<monday>.json`, with its SHA-256 in `picks/SHA256SUMS`.

- 2026-10-13: the freeze's `closest` field before 2026-10-19 was matched on no closed bars and isn't used; the scored pick is `picks/<monday>.json`. The 2026-10-12 pick was posted on X on Mon 12 Oct 11:06 UTC and added here on Tue 13 Oct. Published freezes are never edited.
- 2026-10-13: the week of 12 Oct was frozen twice: by our server at 00:01 UTC (sha256 01b9123dbf6ef6b696fd08b7b384ad2b1d594826c2afa61483c0a8860da54fba, still served at https://edgewise.to/api/weekly-freeze/BTC/2026-10-12) and by a backup job at 00:30 UTC (sha256 d8496a22…, the file published here). The two differ only in `closest` (the five closest weeks, not used before 2026-10-19, see above), `app_commit` (the version of the app that computed each) and `computed_at` (when each was computed). The band, which is what gets scored, is identical. From 19 Oct the freeze will hold the band only, and the backup job will publish the server's stored file instead of computing its own.

## Timestamp proofs (from the week of 19 Oct 2026)

Each freeze's SHA-256 is stamped with OpenTimestamps when it is frozen; the proof is `frozen/<monday>_btc.json.ots`. On Monday around 06:00 UTC a job upgrades it to a Bitcoin block and commits the upgrade only when `scripts/ots_check.py` shows that the proof commits to the committed JSON and that its Bitcoin attestation matches the chain (two block explorers). Check it yourself: `ots verify frozen/<monday>_btc.json.ots` with a Bitcoin node, or `python scripts/ots_check.py frozen/<monday>_btc.json frozen/<monday>_btc.json.ots` without one. There is no proof for the week of 12 Oct, and none will be made: a stamp made later would only prove the later date.
