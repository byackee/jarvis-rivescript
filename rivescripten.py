#!/usr/bin/python
import sys
import re
from rivescript import RiveScript

rs = RiveScript(utf8=True)
rs.unicode_punctuation = re.compile(r'[.,!?;:]')
rs.load_directory("./plugins/jarvis-rivescript/eg/brain/en")
rs.sort_replies()

msg = sys.argv[1]
reply = rs.reply("localuser", msg)
print(reply)

# vim:expandtab
