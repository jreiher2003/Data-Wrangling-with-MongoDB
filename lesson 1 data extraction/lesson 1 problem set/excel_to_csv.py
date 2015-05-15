import xlrd
import csv
import os



def parse_file(df):
	workbook = xlrd.open_workbook(df, 'r')
	sheet = workbook.sheet_by_index(0)
	print sheet.nrows

print parse_file('2013_ERCOT_Hourly_Load_Data')
