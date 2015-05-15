#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import xlwt, csv
import codecs
import sys

wb = xlwt.Workbook()
ws = wb.add_sheet('testSheet')

with codecs.open('beatles-diskography', 'rb', encoding='utf-8') as f:
	f.write('new_beatles.csv')
