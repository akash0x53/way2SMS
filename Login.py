#! /usr/bin/env python
import gtk

class Login():

	def __init__(self):
		self.builder=gtk.Builder()
		self.builder.add_from_file("./ui/w2s.glade")

		self.login=self.builder.get_object("login")

			
		res=self.login.run()

		if(res==1):
			print "logged in"
			
		elif(res==2):
			pass

		self.login.hide()
	
		


if(__name__=="__main__"):
	l=Login()
	gtk.main()
	del l

