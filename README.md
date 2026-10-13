# Edgewise weekly: Bitcoin's week, frozen on Monday, checked on Saturday

Every Monday, Edgewise publishes how Bitcoin's week could play out. Every Saturday, it checks that against what
actually happened. This repository holds the Monday reads, frozen before the week plays out, so anyone can check that
nothing was changed afterwards.

## What gets frozen each Monday (UTC)

- **00:05**: Bitcoin's week band, as the Edgewise app shows it at the week's open. It is the middle 20 / 40 / 60 / 80%
  of where Bitcoin's last 104 weeks closed, measured from the open, at every hour of the week.
  Over 248 tested weeks, Bitcoin closed inside the 80% band 83% of the time. That means a miss about one week in five,
  and two in a row do happen.
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
