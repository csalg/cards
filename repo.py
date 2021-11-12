import os

from tinydb import TinyDB, Query
from dataclasses import asdict
import time

DB_PATH = os.path.join(os.path.dirname(__file__), 'db.json')
LOCK_PATH = os.path.join(os.path.dirname(__file__),'.lock')


class ItemRepository:
  def __init__(self):
    self.db = TinyDB(DB_PATH)

  def save_items(self, items):
    self.lock()
    Item = Query()
    for item in items:
      if len(self.db.search(Item.thumbnail == item.thumbnail)):
        continue
      self.db.insert({**asdict(item), 'timestamp': now()})
    self.unlock()

  def mark_older_as_seen(self, timestamp):
    self.lock()
    Item = Query()
    for item in self.db.search(Item.timestamp < timestamp):
      if item['seen']:
        continue
      self.db.remove(Item.url == item['url'])
      item['seen'] = True
      self.db.insert(item)
    self.unlock()

  def get_unseen_items(self):
    Item = Query()
    return self.db.search(Item.seen == False)

  def lock(self):
    print('Trying to acquire lock')
    if os.path.exists(LOCK_PATH):
      time.sleep(1)
      print('Could not acquire lock. Will retry in 1 second.')
      return self.lock()
    with open(LOCK_PATH, 'w') as file:
      file.write('')
    print('Acquired lock')

  def unlock(self):
    if os.path.exists(LOCK_PATH):
      os.remove(LOCK_PATH)
    print('Lock released')



def now():
  return int(time.time())