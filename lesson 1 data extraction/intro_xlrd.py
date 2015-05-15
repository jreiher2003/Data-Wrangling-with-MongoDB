import xlrd

def parse_file(df):
	workbook = xlrd.open_workbook(df)
	sheet = workbook.sheet_by_index(0)

	data = [[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

	print  "\nList Comprehension"
	print "data[3][2]:", data[3][2]

	print "\nCells in a nested loop:"
	for row in range(sheet.nrows):
		for col in range(sheet.ncols):
			if row == 50:
				print sheet.cell_value(row,col),

	print sheet.cell_type(2,2)
	print sheet.cell_value(2,2)
	exceltime = sheet.cell_value(1,0)
	print exceltime
	print xlrd.xldate_as_tuple(exceltime, 0)

parse_file('2013_ERCOT_Hourly_Load_Data.xls')