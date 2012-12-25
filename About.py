#! /usr/bin/env python

import gtk

class About():

	def __init__(self):

		builder=gtk.Builder()
		builder.add_from_file("./ui/about.glade")
		abt_dialog=builder.get_object("about")

		abt_dialog.run()
		abt_dialog.hide()


#if(__name__=="__main__"):
#	a=About()
#	gtk.main()

