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

		#random_server_no=random.randint(1,11)
		Connect.server="http://site"+str(random_server_no)+".way2sms.com"
	
		#print __cookies__
		
		#cookies=cl.CookieJar()
		self.redirect=ul2.HTTPRedirectHandler()
		#NOTE:if you want to have proxy, use this handler. put proxies in opener
		proxies=ul2.ProxyHandler(self.proxy) 

		Connect.opener=ul2.build_opener(ul2.HTTPCookieProcessor(__cookies__),self.redirect)
		Connect.opener.addheaders=[('User-agent',user_agent),
					('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
					('Accept-Language','en-US,en;q=0.8')]

	
	def login(self,usr,pwd):
		try:
			#print usr,pwd
			response=Connect.opener.open(Connect.server+"/Login1.action","username="+usr+"&password="+pwd)
			redirected_url=response.geturl()
			print redirected_url
			check_session_id=urlparse.urlparse(redirected_url)
			Connect.session_id=check_session_id[len(check_session_id)-2]
			print Connect.server

			if(len(Connect.session_id)<=10): #NOTE session_id<=3|10
				print 'Wrong mobile number or password'
				return login_failed
			else:
				print "Session id: "+Connect.session_id

				return login_success

		except IOError:
			print 'Network Error.!'

	

	def getContacts(self):
		#generate token=Session_ID
		Connect.token=list()
		for i in range(3,len(Connect.session_id)):
			Connect.token.append(Connect.session_id[i])
		#print Connect.token

		response=Connect.opener.open(Connect.server+"/QuickContacts","folder=dashboard&Token="+''.join(Connect.token))
		return response.read()

	def logout(self):
		response=Connect.opener.open(Connect.server+"/LogOut","folder=inbox&token="+''.join(Connect.token))

	def send_msg(self,number,msg):
		response=Connect.opener.open(Connect.server+"/quicksms.action","HiddenAction=instantsms&expensive=sdf44557df54&MobNo="+number+"&textArea="+msg+"&embassy="+''.join(Connect.token))

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

	def add_contact(self,name,no):
		body="HiddenAction=UserContacts&hidval=0&groupCombo=0&tfContactName="+name+"&tfMobileNum="+no+"&hidgrp=1&cmbgrp=0&select2=main&txta_contacts=aaa&Token="+''.join(Connect.token)

		response=Connect.opener.open(Connect.server+"/FirstServlet",body)
		response=response.geturl()

		#print response
		if(response.find("Exist")>0):
			#print 'Contact exist'
			return False
		elif(response.find("added")>0):
			return True
				

