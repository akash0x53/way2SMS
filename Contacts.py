#! /usr/bin/env python

# Way2SMS Desktop-App
# Author: Akash Shende
# Contact: akash321@gmail.com


from bs4 import BeautifulSoup as bs
from way2sms import __contact_list__


class Contacts():

	def __init__(self,html_data,c_list):
		#creating soup
		Contacts.soup=bs(''.join(html_data))
		
		Contacts.c_list=c_list
		
	def extract_name(self):
		names=Contacts.soup.findAll(attrs={"name":"Quckvalue"})
		print names
		names=str(names[0]['value'])
		name_list=names.split("*")
		

		#for n in name_list:
		#	print n,"\n"

		return name_list

	def extract_number(self):
		numbers=Contacts.soup.findAll(attrs={"name":"Qucktitle"})
		numbers=str(numbers[0]['value'])
		number_list=numbers.split(',')

		#for n in number_list:
		#	print n,"\n"

		return number_list
	
	def build_list(self):

		list1=self.extract_name()
		list2=self.extract_number()
		
		for i in xrange(1,len(list1)):
			Contacts.c_list.append([str(list1[i]),str(list2[i])])

	






