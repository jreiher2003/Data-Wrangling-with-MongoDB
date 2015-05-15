import xml.etree.ElementTree as ET 
from pprint import pprint

tree = ET.parse('example.xml')
root = tree.getroot()

print "\nChildren of root:"
for child in root:
	print child.tag


title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
	title_text += p.title_text
print "\nTitle:\n", title_text

print "\nAuthor email addresses:"
for a in root.findall('./fm/bibl/aug/au'):
	email = a.find('email')
	if email is not None:
		print email.text
		
#'  append',
#  'attrib',
#  'clear',
#  'copy',
#  'extend',
#  'find',
#  'findall',
#  'findtext',
#  'get',
#  'getchildren',
#  'getiterator',
#  'insert',
#  'items',
#  'iter',
#  'iterfind',
#  'itertext',
#  'keys',
#  'makeelement',
#  'remove',
#  'set',
#  'tag',
#  'tail',
#  'text'