from pymongo import MongoClient
import csv
import json
import io
import re
from pprint import pprint

field_map = {
	"name" : "name",
    "bodyStyle_label" : "bodyStyle",
    "assembly_label" : "assembly",
    "class_label" : "class",
    "designer_label" : "designer",
    "engine_label" : "engine",
    "length" : "length",
    "height" : "height",
    "width" : "width",
    "weight" : "weight",
    "wheelbase" : "wheelbase",
    "layout_label" : "layout",
    "manufacturer_label" : "manufacturer",
    "modelEndYear" : "modelEndYear",
    "modelStartYear" : "modelStartYear",
    "predecessorLabel" : "predecessorLabel",
    "productionStartYear" : "productionStartYear",
    "productionEndYear" : "productionEndYear",
    "transmission" : "transmission"
}

fields = field_map.keys()

def skip_lines(input_file, skip):
	for i in range(0, skip):
		next(input_file)

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def strip_automobile(v):
	return re.sub(r"\s*\(automobile\)\s*", " ", v)

def strip_city(v):
	return re.sub(r"\s*\(city\)\s*", " ", v)

def parse_array(v):
	if (v[0] == "{") and (v[-1] == "}"):
		v = v.lstrip("{")
		v = v.rstrip("}")
		v_array = v.split("|")
		v_array = [i.strip() for i in v_array]
		return v_array
	return v

def mm_to_meters(v):
	if v < .01:
		return v * 1000
	return v

def clean_dimension(d, field, v):
	if is_number(v):
		if field == 'weight':
			d[field] = float(v) / 1000.0
		else:
			d[field] = mm_to_meters(float(v))

def clean_year(d, field, v):
	d[field] = v[0:4]

def parse_array2(v):
	if (v[0] == "{") and (v[-1] == "}"):
		v = v.lstrip("{")
		v = v.rstript("}")
		v_array = v.split("|")
		v_array = [i.strip() for i in v_array]
		return (True, v_array)
	return (False, v)

def ensure_not_array(v):
	(is_array, v) = parse_array(v)
	if is_array:
		return v[0]
	return v 

def ensure_array(v):
	(is_array, v) = parse_array2(v)
	if is_array:
		return v
	return [v]

def ensure_float(v):
	if is_number(v):
		return float(v)

def ensure_int(v):
	if is_number(v):
		return int(v)

def ensure_year_array(val):
	vals = ensure_array(val)
	year_vals = []
	for v in vals:
		v = v[0:4]
		v = int(v)
		if v:
			year_vals.append(v)
	return year_vals

def empty_val(vals):
	val = val.strip()
	return (val == "NULL") or (val == "")

def years(row, start_field, end_field):
	start_val = row[start_field]
	end_val = row[end_field]

	if empty_val(start_val) or empty_val(end_val):
		return []

	start_years = ensure_year_array(start_val)
	if start_years:
		start_years = sorted(start_years)
	end_years = ensure_year_array(end_val)
	if end_years:
		end_years = sorted(end_years)
	all_years = []
	if start_years and end_years:
		for i in range(0, min(len(start_years), len(end_years))):
			for y in range(start_years[i], end_years[i] + 1):
				all_years.append(y)
	return all_years

def process_file(input_file):
	pass