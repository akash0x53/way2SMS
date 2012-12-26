import httplib as hl
import random
import urllib as ul
import urllib2 as ul2
import cookielib as cl

#global Cookiejar
__cookies__=cl.CookieJar()


#return values
login_failed=-1
login_success=1


__send_button__=None

