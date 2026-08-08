import json
import os

with open(os.path.expanduser("~/.shell4/config/language"), "r") as f:
    _lang = f.read()

def load():
    global lang
    with open(os.path.expanduser(f"~/.shell4/languages/{_lang}.lang"), "r") as f:
        lang = json.loads(f.read())