#! /usr/bin/env python

import gtk

class Credentials():

	def __init__(self):

		builder=gtk.Builder()
		builder.add_from_file("./ui/w2s.glade")
		dialog=builder.get_object("login_save")

		usrname=builder.get_object("id")
		pass1=builder.get_object("pass1")
		pass2=builder.get_object("pass2")


		res=dialog.run()
		print res
		dialog.hide()
		
		try:
			pass_file=open(".pass",'w')
			pass_file.write(str(usrname.get_text())+"\n")
			pass_file.write(str(pass2.get_text()))
			pass_file.close()
		except IOError:
			print('File can not open')

		finally:
			pass_file.close()
			



if(__name__=="__main__"):
	a=Credentials()



