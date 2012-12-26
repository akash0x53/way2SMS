#! /usr/bin/env python

from way2sms import *
from way2sms import __cookies__
#from way2sms import login_failed
from Contacts import Contacts

import urlparse

#global __cookies__
#data={'mobileNo':'',
#		'message':'',
#		'username':'8055737517',
#		'password':'**********',
#		'userLogin':'No'
#		}
#
#ul.urlencode(data)
#data="mobileNo=&message=&username=9849422122&password=sdad&userLogin=no"
#cookie="__gads=ID=b15250aafecdc737:T=1355214097:S=ALNI_MYrKUe01lLEb_cEdPfUIOF9FjlHdg;"
#header={ 'Host':'site1.way2sms.com',
#		'Cookie':cookie,
#		'User-Agent':'Mozilla/5.0',
#		'Content-type':'application/x-www-form-urlencoded',
#		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#		'Referer':'http://site1.way2sms.com/entry.action?id=',
#		'Accept-Encoding':'gzip,deflate,sdch',
#		'Accept-Language':'en-US,en;q=0.8',
#		}
#


class Connect():

	def __init__(self):
		self.proxy={'http':'http://localhost:8080'}
		#print __cookies__
		
		#cookies=cl.CookieJar()
		self.redirect=ul2.HTTPRedirectHandler()
		#proxies=ul2.ProxyHandler(proxy)

		Connect.opener=ul2.build_opener(ul2.HTTPCookieProcessor(__cookies__),self.redirect)

	
	def login(self,usr,pwd):
		try:

			print usr,pwd
			response=Connect.opener.open("http://site1.way2sms.com/Login1.action","username="+usr+"&password="+pwd)
			redirected_url=response.geturl()
			check_session_id=urlparse.urlparse(redirected_url)
			session_id=check_session_id[len(check_session_id)-2]

			if(len(session_id)<=10): #NOTE session_id<=3|10
				print 'Wrong mobile number or password'
				return login_failed
			else:
				print "Session id: "+session_id
				return login_success

		except IOError:
			print 'Network Error.!'

	

	def getContacts(self):
		response=Connect.opener.open("http://site1.way2sms.com/QuickContacts","folder=dashboard")
		return response.read()



if(__name__=='__main__'):

	c=Connect()
	

	print c.login("8055737517","lovetakesover")
	g=Contacts(c.getContacts())

	g.extract_name()
	g.extract_number()
	#print g


