#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete <keyword> - delete keyword.
# py.exe mcb.pyw delete - delete all keywords.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] == 'delete':
        mcbShelf.clear()
mcbShelf.close()
