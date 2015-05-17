from autos import process_file
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.uda
# def insert_autos(infile, db):
     
    # Add your code here. Insert the data in one command.
    
  
if __name__ == "__main__":
    # Code here is for local use on your own computer.
    data = process_file('small_autos.csv')
    pprint(data)
    db.autos.insert(data)
    # insert_autos('small_autos.csv', db)
    pprint(db.autos.find_one())