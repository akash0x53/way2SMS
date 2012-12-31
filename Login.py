#! /usr/bin/env python

# Way2SMS Desktop-App
# Author: Akash Shende
# Contact: akash321@gmail.com

import gtk


from way2sms import *
from Connect import Connect
from Contacts import Contacts

class Login():
	
	def __init__(self,btn,c_list):

		self.builder=gtk.Builder()
		self.builder.add_from_file("./ui/w2s.glade")

		self.login=self.builder.get_object("login")

		usr=self.builder.get_object("usr")
		pwd=self.builder.get_object("pwd")

		msg_box=gtk.MessageDialog(parent=None,type=gtk.MESSAGE_ERROR,buttons=gtk.BUTTONS_OK)
		msg_box.set_markup("Invalid Mobile Number or Password")

		Login.btn=btn
		Login.c_list=c_list

		
		# FIXME: Autologin
		#try:
		#	pass_file=open(".pass","r")
		#	usr.set_text(pass_file.read().rsplit()[0])
		#	pass_file.close()
		#except IOError:
		#	print('file cant open')
		#
		#finally:
		#	pass_file.close()

		res=self.login.run()

		if(res==1):
			Login.con=Connect()
			
			state=Login.con.login(usr.get_text(),pwd.get_text())

			if(state==login_failed):
				msg_box.run()
				msg_box.hide()
			elif(state==login_success):
				contact=Contacts(Login.con.getContacts(),Login.c_list)
				contact.build_list()
				Login.btn.set_sensitive(True)
				
				#fetch contatcs data
	
		
		elif(res==2):
			pass

		self.login.hide()

	def logout(self):
		Login.con.logout()

	def send_msg(self,number,msg):
		return Login.con.send_msg(number,msg)

	def add_contact(self,name,no):
		return Login.con.add_contact(name,no)



