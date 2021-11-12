
from flask import Flask, render_template
import re

from repo import ItemRepository, now
from model import Card

app = Flask(__name__)
FILENAME = 'routines.project'

# TODO Have an index with project files from the project folder
# TODO Have a viewer for any file
# TODO Have a cache for images

@app.route('/')
def results():  # put application's code here
  # Read sample.project
  with open(FILENAME) as file:
    lines = file.readlines()
  # Find out the line numbers where cards start and end and split the text accordingly
  previous_card_start = 0
  card_line_indexes = [] # The start and end line indexes of each card
  previous_card_was_image = False
  for i, line in enumerate(lines):
    if i == 0:
      continue
    if not line.strip('\n'):
      continue
    new_card_because_shebang = re.match(r"^! .*", line)
    new_card_because_image = re.match(r"^http.*", line)
    if new_card_because_shebang or new_card_because_image or previous_card_was_image:
      card_line_indexes.append( (previous_card_start, i) )
      previous_card_start = i
    if previous_card_was_image:
      previous_card_was_image = False
    if new_card_because_image:
      previous_card_was_image = True
    
  if previous_card_start < len(lines):
    card_line_indexes.append( (previous_card_start, len(lines)) )

  # Render cards
  card_renders =  list(map(lambda index: Card.from_card_lines(lines[index[0]:index[1]]).render(), card_line_indexes))

  # Pass the render on to template
  return render_template('index.html.j2', cards=card_renders)

if __name__ == '__main__':
  app.run()
