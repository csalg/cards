from dataclasses import dataclass

import re
import markdown


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
      images = re.findall(r"^http.*", ''.join(card).strip('\n'))
      image = None
      if images:
          image = images[0]
      body = None
      # If we don't have an image, then the card is title + body type card
      if not image:
          # Edge case: Card with single line body and no title
          if (len(card) == 1) and (not title):
              body = card[0]
          elif not title:
              body = "\n".join(card)
          else:
              body = "\n".join(card[1:])
      return cls(title, body, image)


    def render(self):
      if self.image:
          return f"<img src='{self.image}'>"
      else:
          body = ""
          if self.body:
              body = markdown.markdown(self.body)
          title = ""
          if self.title:
              newline = '\n'
              title = f"<h1>{self.title.strip(newline)}</h1>"
          return title + body

