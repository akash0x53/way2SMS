#! /usr/bin/env python

from way2sms import *

hl.HTTPConnection.set_debuglevel=100
#creating HTTP connection
conn=hl.HTTPConnection('site1.way2sms.com',80)
conn.connect()

#http request
req=conn.putrequest('GET','/content/index.html')
conn.endheaders()
conn.send("")
res=conn.getresponse()

print res.read()
