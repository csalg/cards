from dataclasses import dataclass

import re
import os
import markdown
import toml

with open('config.toml') as file:
    config = toml.load(file)

CACHE_ADDRESS = config['cache_address']

@dataclass
class Card:
    title: str
    body: str
    image: str
    
    @classmethod
    def from_card_lines(cls, card):
      if not len(card):
          raise Exception('No lines received!')
          
      title = card[0].strip('! ') if re.match(r"^! .*", card[0]) else None
      images = []
      for line in card:
          if re.findall(r"^http.*",line) or re.findall(r".*(jpg|png)",line):
              images.append(line)

      image = None
      if images:
          image = images[0]
          body = "\n".join(card[1:])
          return cls(title, body, image)
      else:
          # Edge case: Card with single line body and no title
          if (len(card) == 1) and (not title):
              body = card[0]
          elif not title:
              body = "\n".join(card)
          else:
              body = "\n".join(card[1:])
      return cls(title, body, image)

    @classmethod
    def from_gallery_line(cls, line, project_folder_path):
        gallery_path = line.strip("@gallery:").rstrip()
        path = os.path.join(project_folder_path, gallery_path)
        print(path)
        cards = []
        for root, _, filenames in os.walk(path, topdown=False):
            for filename in filenames:
                path_ = os.path.join(root, filename)
                cards.append(cls("", "", "local:"+path_))
        return cards


    def render(self):
        body = ""
        if self.body:
          body = markdown.markdown(self.body)
        if self.image:
          address = f'{CACHE_ADDRESS}/files/{self.image}'
          if re.match(r"^http.*", self.image):
              address = f"{CACHE_ADDRESS}/{self.image}"
          if re.match(r'^local:', self.image):
              address = f'/local?path={self.image[6:]}'

          return f"<img src='{address}'><div>{body}</div>"
        else:
          title = ""
          if self.title:
              newline = '\n'
              title = f"<h1>{self.title.strip(newline)}</h1>"
          return title + body

