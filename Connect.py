#! /usr/bin/env python

# Way2SMS Desktop-App
# Author: Akash Shende
# Contact: akash321@gmail.com


from way2sms import *
from way2sms import __cookies__
from Contacts import Contacts
import urlparse


user_agent="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11"

class Connect():

	def __init__(self):
		self.proxy={'http':'http://localhost:8080'}
		#print __cookies__
		
		#cookies=cl.CookieJar()
		self.redirect=ul2.HTTPRedirectHandler()
		proxies=ul2.ProxyHandler(self.proxy)

		Connect.opener=ul2.build_opener(ul2.HTTPCookieProcessor(__cookies__),self.redirect)
		Connect.opener.addheaders=[('User-agent',user_agent),
					('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
					('Accept-Language','en-US,en;q=0.8')]

	
	def login(self,usr,pwd):
		try:

			#print usr,pwd
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

	def logout(self):
		response=Connect.opener.open("http://site1.way2sms.com/LogOut","folder=inbox")

	def send_msg(self,number,msg):
		response=Connect.opener.open("http://site1.way2sms.com/quicksms.action","HiddenAction=instantsms&Action=sdf44557df54&MobNo="+number+"&textArea="+msg)

		#print response.geturl()

		temp=response.geturl()
		cnt=temp.find("successfully")

		if(cnt<=0):
			print 'sending failed'
			return False
		else:
			print 'sent'
			return True

		#print urlparse.urlparse(response.geturl())[2]
				

