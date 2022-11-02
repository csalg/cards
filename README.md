# Improving `Cards`

I think of all the programs I have written, `cards` is the one I use the most often.

I think I never cease to find uses for it. When I need to write some clear notes on something, `cards` makes it trivial.

Initially, I used cards to collect lots of photos of menswear and basically educate myself on the subject. It's a great tool to conduct research on something because it creating a board is so easy.

I think, however, the concept can be expanded a bit.

Some possible features:

### Linking between boards and cards

Unlike with Zettelkasten, the basic unit of cards is a board. I think it would be nice to introduce some meta tags for cards. This would make them addressable.

Suppose I want to address a board, I could write `@a:<board-path>` which will show the title of the first card of the board linking to the board.

`@a:<board-path>/<card-perm>` links to the card. For this, the card needs to have an `@perm:` tag.

Additional attributes for tags could be encoded like this: `<tag-name>.<key>=val:<payload>`.

This would allow having `@a.snippet=first-card.<board-path>` to insert the first card of the board as a link to the board (as opposed to just the title without spawning a new card).

### Cards as atoms

So I would create a folder with files, and these files would have cards in them just like now. But each card would have a perm (I guess I could generate these automatically to avoid the trouble of having to do so by hand).

Then when these are opened only the first card is displayed (possibly a summary card). Then I would click around and create the board of the path. These paths could then be saved.

Of course I don't really know if this makes a lot of sense. Maybe saving paths is not very important.

### Use cases

I find myself creating lots of folders. Whenever I want to put some order in some part of my life, I create a board. And this allows me to see the big picture and capture all sorts of details to offload my brain. But the **proliferation of project folders** is a problem. Introducing linking means I could have many boards but not have to expose them. 

Also I sometimes just create boards and forget the point of that board or how it differs from other boards.

### Dynamic content

For example, I want to keep track of Facebook posts in a group, or results for certain dba queries. Then I would want some way of 1) converting a certain url to json, 2) interpretting that json, inferring whether there are new items, and storing them in a db, and 3) converting those objects into a view. Still, it's fairly trivial because all I need to do is generalize the jinja2 template a bit so it can be used more widely.

### Filtering

It would be great if I could filter the cards. It's more or less trivial with vanilla javascript, though.

### Rendering other stuff, e.g. markdown or csv files

The pain point here is that it's not clear where different types of projects should live, or indeed what those types are, or whether a project is of a certain type. One can expect that health, fitness, nutrition can be modeled as three or one project. But whatever the case, there will likely be markdown and csv files around. Photos too, but those I can deal with.

### Have tooling for converting folder with photos into `.cards` file and photos in server cache.

This would be useful for e.g. body pics or taking screencaps of some video and commenting it.
