# Links between note
## Rationale
Sometime, you want to relate note together. The idea is pretty simple,
it's the same than the one behind wikis and behind the web. In a note,
you make a reference to the content another note. You may naturally
want to create a link, which allow to open see the other note.

## How to create a link
There are currently three ways to add a link with this add-on.

### Simple way
You add the note id directly in a field. When the field content is
displayed, any number with at least 12 digits will be transformed into
a link, which will open the browser and show this note.

### Buttons
In the editor, you have two new buttons. You need to select text and click on one of the button. The button "link to note" ![Link to note](icons/note.svg) takes a note id, and create a link to this note id. The button "Link to browser search" ![Link to browser search](icons/browser.svg) take any search, put it in the browser search bar, and search it.

### HTML
If you know how to edit html, you can the javascript action `pycmd("browser search:query")` to show the result of the search "query" in the browser. In particular, you can use the query "nid:012345678910" to search the note with id 012345678910.

You can edit a note by selecting a field and pressing ctrl+shift+x. Or by installing the add-on [Show field's source (html) in editor](https://ankiweb.net/shared/info/1574324795).

## How to get note id
There exists at least two ways to get a note id. In the browser, select a card, select "cards > info" or "Ctrl+Shift+I", a pop-up will show you a lot of information about the card. You want to copy "Note ID".

The add-on [Advanced browser](https://ankiweb.net/shared/info/874215009) has an internal column "Note ID". It allows you to see quickly see the id of a note. Starting with Anki 2.1.24, you can double click on it in order to select it and copy it (You need to set its configuration "Table content" to "Selectable" for it to work.)

## Advice
You may want to consider installing the add-on [Opening the same window multiple time](https://ankiweb.net/shared/info/354407385), so that you can have multiple instance of the browser opened at the same time and see your note in a new window.

## Warning
This will not work in ankidroid, ios, ankiweb, or when the add-on is not installed.

## TODO
* Allow link to cards ?
* Link works in editor too.
* In browser, allow to use click and drag to add a link directly.
* Allow to give name to notes to use in search/use other search

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
            | Add hyperlink addon, maintened by @ijgnd, anonymous, probably reddit user /u/NavyTeal, see [reddit](https://www.reddit.com/r/Anki/comments/9t7acy/bringing_markdown_to_anki_21/), and some code from the Power Format Pack: Copyright 2014-2017 Stefan van den Akker <neftas@protonmail.com> , 
License     | GNU GPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-link-to-other-card
Addon number| [2053932397](https://ankiweb.net/shared/info/2053932397)
