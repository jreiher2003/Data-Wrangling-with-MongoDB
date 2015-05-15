#!/usr/bin/env python
from pymongo import MongoClient	

def porsche_query():
	query = {"manufacturer_label" : "Porsche"}
	return query

def get_db(db_name):
	client = MongoClient('mongodb://localhost:27017')
	db = client[db_name]
	return db

def find_porsche(db, query):
	return db.autos.find(query)

if __name__ == '__main__':
	db = get_db('uda')
	query = porsche_query()
	find_porsche(db, query)
