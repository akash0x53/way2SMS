#! /usr/bin/env python

import pygtk
import gtk


import About
import Login
#import Credentials

count=140

class Sender():

	def __init__(self):
		self.build=gtk.Builder()
		self.glade=self.build.add_from_file("./ui/w2s.glade")


		self.ext_menu=self.build.get_object("exit")
		self.ext_menu.connect("activate",gtk.main_quit)

		self.abt_menu=self.build.get_object("about")
		self.abt_menu.connect("activate",self.show_about)

		login=self.build.get_object("login_menu")
		login.connect("activate",self.login_box)

		self.logout=self.build.get_object("logout_menu")
		self.logout.connect("activate",self.logout_now)

		#self.cred=self.build.get_object("credentials")
		#self.cred.connect("activate",self.show_login_save)

		Sender.contacts=self.build.get_object("contact_list")
		
		Sender.snd_btn=self.build.get_object("send_msg")
		Sender.snd_btn.set_sensitive(False)

		Sender.number_txt=self.build.get_object("enter_mobile_no")
		Sender.msg_txt=self.build.get_object("enter_msg")
		Sender.msg_txt.connect("key-press-event",self.check_chars)
	
		Sender.msg_lbl=self.build.get_object("msg_lbl")
		
		clr_btn=self.build.get_object("clr_all")
		clr_btn.connect("clicked",self.clear_all)

		self.win=self.build.get_object("main_win")
		self.win.connect("destroy",gtk.main_quit)
		self.win.show()


	def show_about(self,event):
		abt=About.About()

	def login_box(slef,event):
		Sender.login=Login.Login(Sender.snd_btn,Sender.contacts)
	
	def show_login_save(self,event):
		log_save=Credentials.Credentials()

	def check_chars(self,event,data):
		global count
		buf=""
		Sender.msg_txt.get_buffer()
		print buf
		count-=len(buf)

		Sender.msg_lbl.set_text("Enter Text Message\n"+str(count)+" chars left")
		
	def clear_all(self,event):
		Temp.number_txt.set_text("")
		txt=gtk.TextBuffer()
		txt.set_data("",0)
		Temp.msg_txt.set_buffer(txt)

	def logout_now(self,event):
		try:
			Sender.login.logout()
			del Sender.login
		except:
			print 'You havent logged in, no need to logout dumbo'
	






if(__name__=="__main__"):
	s=Sender()
	gtk.main()

		



