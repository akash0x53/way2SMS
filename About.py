#! /usr/bin/env python

import gtk

class About():

	def __init__(self):

		builder=gtk.Builder()
		builder.add_from_file("./ui/w2s.glade")
		abt_dialog=builder.get_object("about_dialog")

		abt_dialog.run()
		abt_dialog.hide()


