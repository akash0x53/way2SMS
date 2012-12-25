#! /usr/bin/env python

from bs4 import BeautifulSoup as bs


class Contacts():

	def __init__(self,html_data):
		#creating soup
		Contacts.soup=bs(''.join(html_data))
		
	def extract_name(self):
		names=Contacts.soup.findAll(attrs={"name":"Quckvalue"})
		names=str(names[0]['value'])
		name_list=names.split("*")
				
		for n in name_list:
			print n,"\n"

	def extract_number(self):
		numbers=Contacts.soup.findAll(attrs={"name":"Qucktitle"})
		numbers=str(numbers[0]['value'])
		number_list=numbers.split(',')

		for n in number_list:
			print n,"\n"

