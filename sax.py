#!usr/bin/env python

import sys,os,re
from xml.sax import handler,parseString

class LG_Handler(handler.ContentHandler):
	def __init__(self):
		handler.ContentHandler.__init__(self)
		self.content=''
	def startDocument(self):
		print 'Document Start...'
	def endDocument(self):
		print 'Document End...'
	def startElement(self, name, attrs):
		print 'Encounter Element : %s' % (name)
	def endElement(self, name):
		print 'Leave Element : %s ' % (name)
	def characters(self, ch):
		print ch.strip()

if(__name__=='__main__'):
	with open('SCCP_IEBase.xml') as xml_file:
	    parseString(xml_file.read(),LG_Handler())
