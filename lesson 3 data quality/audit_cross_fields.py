import csv
import math
import zipfile
from itertools import islice

def skip_lines(input_file, skip):
	for i in range(0,skip):
		next(input_file)

def is_number(v):
	if v == v.isdigit() and type(v) == int: return True

def ensure_float(v):
	if is_number(v):
		return float(v)

def audit_population_density(input_file):
	for row in input_file:

		population = row['populationTotal']
		# print population
		area = row['areaLand']
		# print area
		population_density = row['populationDensity']
		if population and area and population_density:
			calculated_density = int(population) / int(area)
			print calculated_density
			# if math.fabs(calculated_density - population_density) > 10:
			# 	print "Possibly bad population density for ", row['name']

if __name__ == '__main__':
	input_file = csv.DictReader(open('cities.csv', 'rb'))

	skip_lines(input_file, 3)
	audit_population_density(input_file)