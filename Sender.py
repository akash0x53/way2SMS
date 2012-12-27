#! /usr/bin/env python

import pygtk
import gtk


import About
import Login
#import Credentials

count=140

class Sender():

	def __init__(self):

		Sender.isMaxLimit=False

		self.build=gtk.Builder()
		self.glade=self.build.add_from_file("./ui/w2s.glade")


		self.ext_menu=self.build.get_object("exit")
		self.ext_menu.connect("activate",self.cleanup)

		self.abt_menu=self.build.get_object("about")
		self.abt_menu.connect("activate",self.show_about)

		login=self.build.get_object("login_menu")
		login.connect("activate",self.login_box)

		self.logout=self.build.get_object("logout_menu")
		self.logout.connect("activate",self.logout_now)

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

	
		self.win=self.build.get_object("main_win")
		self.win.connect("destroy",gtk.main_quit)
		self.win.show()


	def max_limit(self,event,data):

		print data
		#print dir(data)

		if(data.keyval=='BackSpace'):
			print "backspace"
			#	return Sender.isMaxLimit


	def send_msg(self,event):
		#start,end=buf.get_selection_bounds()
		msg=Sender.buf.get_text(Sender.buf.get_start_iter(),Sender.buf.get_end_iter())
		number=Sender.number_txt.get_text()
		print "number: "+number+" msg: "+msg
		Sender.login.send_msg(number,msg)



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
	
	def show_login_save(self,event):
		log_save=Credentials.Credentials()

	def check_chars(self,event):
		global count
		length=Sender.buf.get_char_count()+1

		if(length>140):
			print 'Max char limit reached!'
			Sender.isMaxLimit=True
			#Sender.buf.get_text(Sender.buf.get_start_iter(),Sender.buf.get_end_iter()).
		else:
			Sender.isMaxLimit=False

		#count=count-length
	
		#Sender.msg_lbl.set_text("Enter Text Message\n"+str(count)+" chars left")
		
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

		



