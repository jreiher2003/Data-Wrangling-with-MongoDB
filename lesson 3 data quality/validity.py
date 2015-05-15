"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
from itertools import islice

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def valid_year(year):
  if year and year.isdigit():
    year = int(year)
    if year >=1886 and year <=2014:
      return year

def process_file(input_file):

    with open(input_file, "r") as ofile:
        f = csv.DictReader(ofile)
        # reader.next()
        header = f.fieldnames
        # print header
        for row in islice(f,3, None):
            year = row["productionStartYear"]
            year = year.strip().split('-')[0]
            if valid_year(year):
                print row

pfile = process_file(INPUT_FILE)
print pfile
# def write_file(pfile):             
# with open(pfile, "wb") as g:
#     writer = csv.DictWriter(g)
                    # writer.writerow([header])
                    
    # writer.writerow()
                
            # elif not valid_year(year):
            #     not_valid = row

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files

        # with open(output_bad, "w") as b:
        #     writer = csv.DictWriter(b, delimiter=",", fieldnames=header)
        #     # for row in not_valid_year:
        #     #     writer.writerow(row)
        #     # writer.writeheader()
        #     writer.writerow(not_valid)
# 

# def test():

#     process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


# if __name__ == "__main__":
#     test()