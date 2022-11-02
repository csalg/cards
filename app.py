
import re
import os
from dataclasses import dataclass

from flask import Flask, render_template, request, send_file
from model import Card

app = Flask(__name__)

PROJECTS_FOLDER = os.environ['PROJECTS_FOLDER']

@dataclass
class CardsFile:
  path: str
  name: str

  @classmethod
  def from_path(cls, path):
    name = ""
    with open(path, 'r') as file:
      for line in file.readlines():
        if line:
          if line[0] == '!':
            name = line.strip('! ').strip('\n')
            break
      path_without_root = path[len(PROJECTS_FOLDER):]
    return cls(path_without_root, name)


@app.route('/')
def index():
  card_files = []
  for root, _, files in os.walk(PROJECTS_FOLDER, topdown=False):
    for name in files:
      if name[-6:] == '.cards':
        path = os.path.join(root, name)
        card_files.append(CardsFile.from_path(path))
  return render_template('index.html', card_files=card_files)

@app.route('/local')
def serve_local_file():
  path = request.args['path']
  return send_file(path)

@app.route('/card')
def view_cards():  # put application's code here
  path = PROJECTS_FOLDER + request.args['path']
  # Read sample.project
  with open(path) as file:
    lines = file.readlines()
 
  card_line_indexes, gallery_indexes = find_card_start_end_line_indexes(lines)
  # Render cards
  card_renders =  list(map(lambda index: Card.from_card_lines(lines[index[0]:index[1]]).render(), card_line_indexes))
  gallery_renders = []
  for gallery_index in gallery_indexes:
    project_folder_path = os.path.dirname(path)
    for card in Card.from_gallery_line(lines[gallery_index], project_folder_path):
      gallery_renders += [card.render()]

  # Pass the render on to template
  columns = request.args.get('columns', default=4, type=int)
  columns_str = '1fr '*columns
  return render_template('cards.html.j2', cards=card_renders+gallery_renders, cols=columns_str)

def find_card_start_end_line_indexes(cards_file_lines):
   # Find out the line numbers where cards start and end and split the text accordingly
  previous_card_start = 0
  card_line_indexes = [] # The start and end line indexes of each card
  gallery_indexes = []
  # previous_card_was_image = False
  for i, line in enumerate(cards_file_lines):
    if i == 0:
      continue
    if not line.strip('\n'):
      continue
    
    new_card_because_shebang = re.match(r"^!.*", line)
    new_card_because_image = re.match(r"^http.*", line) or re.match(r".*(png|jpg)", line)
    new_card_because_gallery = re.match(r"^\@gallery:.*", line)

    if new_card_because_shebang or new_card_because_image:
      card_line_indexes.append( (previous_card_start, i) )
      previous_card_start = i

    if new_card_because_gallery:
      gallery_indexes.append(i)

  if previous_card_start < len(cards_file_lines):
    # TODO: Handle if last is gallery
    card_line_indexes.append( (previous_card_start, len(cards_file_lines)) )

  return card_line_indexes, gallery_indexes

if __name__ == '__main__':
  app.run()
