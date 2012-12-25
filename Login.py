#! /usr/bin/env python
import gtk
import post_req

class Login():

	def __init__(self):
		self.builder=gtk.Builder()
		self.builder.add_from_file("./ui/w2s.glade")

		self.login=self.builder.get_object("login")

		usr=self.builder.get_object("usr")
		pwd=self.builder.get_object("pwd")
		
		try:
			pass_file=open(".pass","r")
			usr.set_text(pass_file.read().rsplit()[0])
			pass_file.close()
		except IOError:
			print('file cant open')

		finally:
			pass_file.close()


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

