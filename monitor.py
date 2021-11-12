import os
import time

from model import Item
from bs4 import BeautifulSoup
import requests
import toml

from repo import ItemRepository

with open(os.path.join(os.path.dirname(__file__), 'config.toml')) as file:
  config = toml.load(file)

repo = ItemRepository()

def fetch():
  page = requests.get("SOME_PAGE")
  soup = BeautifulSoup(page.content, 'html.parser')
  # And so it goes
  pass

if __name__ == '__main__':
  while True:
    fetch()
    time.sleep(config['monitor']['wait'])

