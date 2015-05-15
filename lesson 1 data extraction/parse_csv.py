import pprint
import csv
data = []
with open('beatles-diskography.csv', 'rt') as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append(row)

    pprint.pprint(data)

    
# import os
# import csv

# def parse_file(df):
# 	reader = csv.reader(open(df, 'r'))
# 	d = {}
# 	for row in reader:
# 		key = row[0]
# 		if key in d:
# 			pass
# 		d[key] = row[1:]
# 	print d

# print parse_file('beatles-diskography.csv')
# import pprint
# import csv
# reader = csv.DictReader(open('beatles-diskography.csv'))

# result = {}
# for row in reader:
#     for column, value in row.iteritems():
#         result.setdefault(column, []).append(value)
# pprint.pprint(result)
