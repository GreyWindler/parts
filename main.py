#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,re

migrations = '/Migrations/'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
	find = input("Введите строку:")
	list_files = os.listdir(current_dir + migrations)
	i=0
	for file in list_files:
		filename, file_extension = os.path.splitext(str(current_dir + migrations + file))
		if "sql" in file_extension and find in open(filename + file_extension).read():
			print(filename + file_extension)
			i+=1
	print (i)
pass
