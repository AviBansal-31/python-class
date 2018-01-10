# bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#http://www.dr-chuck.com
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() #read it all
soup = BeautifulSoup(html, 'html.parser')

# retrieve anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# print a dict
