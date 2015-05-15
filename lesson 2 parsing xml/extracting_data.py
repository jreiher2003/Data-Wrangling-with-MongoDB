#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys
# 

import xml.etree.ElementTree as ET 
from pprint import pprint

tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

# for child in root:
# 	print child.tag
	# print child.tail
	# print child.text
 
def info():
	authors = []
	for a in root.findall('./fm/bibl/aug/au'):
		d = {
			'snm': None,
			'fnm': None,
			'email': None
		}
		d['snm'] = a.find('snm').text
		d['fnm'] = a.find('fnm').text
		d['email'] = a.find('email').text

		authors.append(d)
	return authors

	
# pprint(info())

