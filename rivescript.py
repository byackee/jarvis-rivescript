#!/usr/bin/python
import sys
from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("./eg/brain")
rs.sort_replies()

msg = sys.argv[1]
reply = rs.reply("localuser", msg)
print reply

# vim:expandtab
