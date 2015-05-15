import os
import pprint

def parse_file(df):
	data = []
	with open(df, "rb") as f:
		header = f.readline().split(',')
		counter = 0
		for line in f:
			if counter == 10:
				break
			fields = line.split(",")
			entry = {}

			for i, value in enumerate(fields):
				# print list(enumerate(fields))
				# print i, value
				entry[header[i].strip()] = value.strip()
			data.append(entry)
			counter +=1
	return data

pprint.pprint(parse_file('beatles-diskography.csv'))