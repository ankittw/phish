import urllib2
from urlparse import urlparse
from bs4 import BeautifulSoup
from urlparse import urljoin
from collections import Counter
url_list=[]
domain=[]
path=[]
c=urllib2.urlopen('http://www.gnu.org/software/grub/')
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
	path.append(urlparse(url).path)
	domain.append(urlparse(url).netloc)
print Counter(domain).most_common()
print Counter(path).most_common()
