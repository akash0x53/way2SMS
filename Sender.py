#! /usr/bin/env python

import pygtk
import gtk


import About
import Login
import Credentials



class Temp():

	def __init__(self):
		self.build=gtk.Builder()
		self.glade=self.build.add_from_file("./ui/w2s.glade")


		self.ext_menu=self.build.get_object("exit")
		self.ext_menu.connect("activate",gtk.main_quit)

		self.abt_menu=self.build.get_object("about")
		self.abt_menu.connect("activate",self.show_about)

		self.login=self.build.get_object("login_menu")
		self.login.connect("activate",self.login_box)

		self.cred=self.build.get_object("credentials")
		self.cred.connect("activate",self.show_login_save)

		contacts=self.build.get_object("contact_list")
	

		self.win=self.build.get_object("main_win")
		self.win.connect("destroy",gtk.main_quit)
		self.win.show()


	def show_about(self,event):
		abt=About.About()

	def login_box(slef,event):
		log=Login.Login()
	
	def show_login_save(self,event):
		log_save=Credentials.Credentials()






class Sender():

	def __init__(self):

		self.lbl=gtk.Label("Mobile No")
		Sender.num_txt=gtk.TextView()


		Sender.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		Sender.window.set_title('Way2SMS Desktop App')


		#connecting main_window signal "destroy"
		Sender.window.connect("destroy",gtk.main_quit)

		#horizontal box
		v_box=gtk.VBox(homogeneous=False)
		number=gtk.HBox(homogeneous=True)

		#menu
		connect_menu=gtk.Menu()
	
		main_menu=gtk.MenuItem("Main")
			
		login=gtk.MenuItem("Login")
		credentials=gtk.MenuItem("Credentials")
		
		connect_menu.append(login)
		connect_menu.append(credentials)

		main_menu.set_submenu(connect_menu)

		login.show()
		credentials.show()
		main_menu.show()
		
		#menubar
		menu_bar=gtk.MenuBar()
		menu_bar.append(main_menu)
		#add menubar on HBox
		v_box.pack_start(menu_bar,expand=False,fill=False)
		

		#add hBox to window
		Sender.window.set_border_width(5)
		Sender.window.add(v_box)

		#Menu End---

		#Add mobile no box
		v_box.pack_end(number,expand=False,fill=False)
		number.pack_start(self.lbl)
		number.pack_end(Sender.num_txt)


		#show all
		v_box.show()
		number.show()
		self.lbl.show()
		Sender.num_txt.show()
		menu_bar.show()
		Sender.window.show()
	


if(__name__=="__main__"):
	s=Temp()
	gtk.main()

		



