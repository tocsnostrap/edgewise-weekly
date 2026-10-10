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

Nothing is re-scored or back-filled. A week whose freeze missed its deadline is not scored, and says so.

edgewise.to
