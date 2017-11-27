# coding=utf-8

import urllib
import urllib2

request_data = "%(request_data)s"


url = 'http://127.0.0.1:8080/user'
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
# values = {}
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
print response.code
print type(response.code)

if 0:
    print 000
else:
    print 111
