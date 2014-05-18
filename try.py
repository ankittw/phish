import urllib2
from urlparse import urlparse
from bs4 import BeautifulSoup
from urlparse import urljoin
url_list=[]
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<input href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<input http://chud lo>
<p class="story">...</p>
"""
c=urllib2.urlopen('http://www.wikipedia.com')
soup=BeautifulSoup(c.read())
#soup = BeautifulSoup(html_doc)
for link in soup.find_all('a'):
     url_list.append(link.get('href'))
#print(soup.get_text())    
parse=urlparse('http://www.google.com')
print "hello"
print parse.scheme
print parse.netloc
print parse.path
print parse.geturl()
for url in url_list:
	print urlparse(url).scheme
	print urlparse(url).netloc
