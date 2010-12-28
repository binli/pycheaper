#!/usr/bin/env python
# coding=utf-8
# cheaper - to get more information from some public bbs

import pygtk
pygtk.require('2.0')
import pynotify
import sys
import ConfigParser

s="中文"
s1=u"中文"
s2=unicode(s,"utf-8")
s3=s.decode("utf-8")
print len(s)
print s
print len(s1)
print s1
print len(s2)
print s2
print len(s3)
print s3

notifyTitle = "smth"
notifyContent = "New msg"

if __name__ == '__main__':
	if not pynotify.init("script for monitor"):
		sys.exit(1)
	n = pynotify.Notification(notifyTitle, notifyContent)
	n.set_urgency(pynotify.URGENCY_NORMAL)
	if not n.show():
		print "Failed to send notification"
		sys.exit(1)
