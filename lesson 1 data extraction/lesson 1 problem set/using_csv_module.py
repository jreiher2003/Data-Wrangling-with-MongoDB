import csv
import os

# def open_csv(df):
# 	data = []
# 	with open(df, 'rb') as f:
# 		name = f.readline().split(',')
# 		name = name[1]
# 		header = f.next().split(',')
# 		for line in f:
# 			data.append(line.split(','))
# 		print name
# 		print data[0][1]
# 		print data[2][0]
# 		print data[2][5]
		
# print open_csv('745090.csv')

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        r = csv.reader(f)
        name = r.next()[1]
        header = r.next()
        data = [row for row in r]

    return (name, data)			
			
print parse_file('745090.csv') 
