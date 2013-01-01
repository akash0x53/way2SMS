#! /usr/bin/env python

# Way2SMS Desktop-App
# Author: Akash Shende
# Contact: akash321@gmail.com


import pygtk
import gtk
from way2sms import isMsgSent

import About
import Login
import gtk.keysyms as KeyMap
import os


class Sender():

	def __init__(self):

		Sender.isMaxLimit=False

		self.build=gtk.Builder()
		self.glade=self.build.add_from_file(os.getenv("PWD")+"/ui/w2s.glade")


		self.ext_menu=self.build.get_object("exit")
		self.ext_menu.connect("activate",self.cleanup)

		self.abt_menu=self.build.get_object("about")
		self.abt_menu.connect("activate",self.show_about)

		login=self.build.get_object("login_menu")
		login.connect("activate",self.login_box)

		self.logout=self.build.get_object("logout_menu")
		self.logout.connect("activate",self.logout_now)

		#FIXME: Option Autologin, saving credentials
		#self.cred=self.build.get_object("credentials")
		#self.cred.connect("activate",self.show_login_save)

		Sender.contacts=self.build.get_object("contact_list")
		Sender.table=self.build.get_object("treeview1")
		select=Sender.table.get_selection()
		select.connect("changed",self.select_number)
		
		Sender.snd_btn=self.build.get_object("send_msg")
		Sender.snd_btn.connect("clicked",self.send_msg);
		Sender.snd_btn.set_sensitive(False)

		Sender.number_txt=self.build.get_object("enter_mobile_no")
		Sender.msg_txt=self.build.get_object("enter_msg")
		Sender.buf=Sender.msg_txt.get_buffer()
		Sender.buf.connect("changed",self.check_chars)

		Sender.msg_txt.connect("key-press-event",self.max_limit)
	
		Sender.msg_lbl=self.build.get_object("msg_lbl")
		Sender.name_lbl=self.build.get_object("name_lbl")
		
		clr_btn=self.build.get_object("clr_all")
		clr_btn.connect("clicked",self.clear_all)

		Sender.contact_box=self.build.get_object("contact_add")
		Sender.cont_name=self.build.get_object("contact_name")
		Sender.cont_no=self.build.get_object("contact_no")
		#save_btn=self.build.get_object("save_contact")
		
		cntct_menu=self.build.get_object("contact_menu")
		cntct_menu.connect("activate",self.add_contact)

	
		self.win=self.build.get_object("main_win")
		self.win.connect("destroy",gtk.main_quit)
		self.win.show()

	def add_contact(self,event):

		if(Sender.contact_box.run()==1):
			print 'contact saved'
			print Sender.cont_name.get_text()
			print Sender.cont_no.get_text()

			if(Sender.login.add_contact(Sender.cont_name.get_text(),Sender.cont_no.get_text())):
				msgbox=gtk.MessageDialog(parent=None,type=gtk.MESSAGE_INFO,buttons=gtk.BUTTONS_OK)
				msgbox.set_markup("Contact added")
				msgbox.run()
			else:
				msgbox=gtk.MessageDialog(parent=None,type=gtk.MESSAGE_ERROR,buttons=gtk.BUTTONS_OK)
				msgbox.set_markup("Contact already exist")
				msgbox.run()

			msgbox.hide()	
						
		else:
			print 'canceled'
			pass

		Sender.cont_name.set_text("")
		Sender.cont_no.set_text("")
		Sender.contact_box.hide()


	def max_limit(self,event,data):
		if(data.keyval==KeyMap.BackSpace):
			return False

		return Sender.isMaxLimit


	def send_msg(self,event):
		buf=Sender.msg_txt.get_buffer()
		
		msg=buf.get_text(buf.get_start_iter(),buf.get_end_iter())
		number=Sender.number_txt.get_text()
		#print "number: "+number+" msg: "+msg
		
		isMsgSent=Sender.login.send_msg(number,msg)

		if(isMsgSent==True):
			msg_box=gtk.MessageDialog(parent=self.win,type=gtk.MESSAGE_INFO,buttons=gtk.BUTTONS_OK)
			msg_box.set_markup("Message sent")
			msg_box.run()
			msg_box.hide()

		elif(isMsgSent==False):
			msg_box=gtk.MessageDialog(parent=self.win,type=gtk.MESSAGE_ERROR,buttons=gtk.BUTTONS_OK)
			msg_box.set_markup("Something wrong!\nMessage Sending failed")
			msg_box.run()
			msg_box.hide()


	def select_number(self,select):
		(model,path)=select.get_selected_rows()
	
		for p in path:
			i=model.get_iter(p)
			Sender.number_txt.set_text(model.get_value(i,1))
			Sender.name_lbl.set_text("Mobile Number\n"+model.get_value(i,0))


	def show_about(self,event):
		abt=About.About()

	def login_box(slef,event):
		Sender.login=Login.Login(Sender.snd_btn,Sender.contacts)
	
	#FIXME: Autologin option.
	#def show_login_save(self,event):
	#	log_save=Credentials.Credentials() --- Function removed

	def check_chars(self,event):
		
		length=Sender.buf.get_char_count()+1

		if(length>140):
			print 'Max char limit reached!'
			Sender.msg_lbl.set_text("Maximum character limit reached.")
			Sender.isMaxLimit=True
		else:
			Sender.isMaxLimit=False
			Sender.msg_lbl.set_text("Enter Text Message\n(Max 140 chars")

			
	def clear_all(self,event):
		Sender.number_txt.set_text("")
		txt=gtk.TextBuffer()
		txt.set_data("",0)
		Sender.msg_txt.set_buffer(txt)
		Sender.name_lbl.set_text("Mobile Number")

	def logout_now(self,event):
		try:
			Sender.login.logout()
			Sender.contacts.clear()
			Sender.snd_btn.set_sensitive(False)
			del Sender.login
		except:
			print 'You havent logged in, no need to logout dumbo'

	def cleanup(self,event):
		print 'cleanup'
		try:
			self.logout_now(None)
			print '''
					Thank you for using Way2SMS
					Way2SMS-Desktop App 1.0 Copyright (C) 2012
					Author: Akash Shende
					------------------------------------------\n
					Report bugs, suggestions@ akash321@gmail.com
					visit: akash0x53.github.com
					Fork me https://github.com/akash0x53/way2SMS.git'''
			gtk.main_quit()
		except:
			print "Error: either you haven't connected or your logged out already.\nSystem Exit. Bye. "

	


if(__name__=="__main__"):
	s=Sender()
	gtk.main()

		



