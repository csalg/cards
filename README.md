# Monitor

This is a skeleton repo for monitors.

Monitors are scripts that do two things:
- Periodically do something to fetch data. (monitor.py)
- Present a flask website with that data. (app.py)

The main use of monitors is to save me time looking for 'deals'. Monitors check things constantly and summarize the juicy bits according to some heuristics. Clothes, food, jobs... In this society all of these things can be had for cheap...

# Structure

* **model.py** The data model so that everyone knows what we are talking about. Must have the following fields:
title: string
description: string
url: string
thumbnail: string
seen: boolean
* **repo.py** Obvious what it does.
* **app.py** Flask app
* **monitor.py** Infinite loop with waits. Implement the fetch() procedure.
* **config.toml** Needs to have `monitor.wait`, which is the wait time between fetches.

# Future

- **SQLite** I have some monitors which have been running for a long time, in which case it's not desireable to use TinyDB. I think moving to SQLite would be a good idea, since I am also using it elsewhere.
- **Notifications** This is also something I did for dba / toogoodtogo. This would just be something that is called by the fetch procedure in monitor.py but which is defined in notify.py

# Librarify

If I librarified I could keep on adding generic features. For example, bookmarks, easier notificications, things like that. Some generic features ideas:
- Actions. These avoid having to deal with flask routing by passing an action argument in the query.
- Statistics. Time of day with most activity. This would be quite domain specific, though, so it would only be activity metrics really.
- Bookmarking. This is not so much code either.

I guess the library would be quite simple, but it is also not so clear what the advantage would be.

### Uses
* ebay
* dba
* toogoodtogo
* flight tickets
* amazon
