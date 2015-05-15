#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys, but you have to extract the attributes from the "insr" tag
# and add them to the list for the dictionary key "insr"

import xml.etree.ElementTree as ET 
from pprint import pprint

article_file = 'exampleResearchArticle.xml'

def get_root(fname):
	tree = ET.parse(fname)
	return tree.getroot()

def get_authors(root):
	authors = []
	for author in root.findall('./fm/bibl/aug/au'):
		data = {
				"fnm": None,
				"snm": None,
				"email": None,
				"insr": []
		}
		data["fnm"] = author.find('fnm').text
		data["snm"] = author.find('snm').text
		data["email"] = author.find('email').text
		insr = author.findall('./insr')
		for i in insr:
			data['insr'].append(i.attrib['iid'])

		authors.append(data)
	return authors

root = get_root(article_file)
pprint(get_authors(root))