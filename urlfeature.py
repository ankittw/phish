def dots(url_string):
    count=0
    for char in url_string:
        if char is '.':
            count=count+1

    print count

dots("www.hello.reader./sdas./hi")    

def suspicuous_url(url_string):
	count=0
	for char in url_string:
		if char is '-':
			print "suspicuous URL"
		
suspicuous_url("hhhe-e ee-")
		
			
suspi_words = ["signin","login", "confirm", "account", "secure", "webser" , "ebayisapi" ]



def found_words(str1,str2):
	return  str1   in   str2  
	

def suspi(url_string):
	for word in suspi_words:
		if found_words(word,url_string):
			print "present in list"
			
			
suspi("signin my friendlogin")			






file = open('tld','r')
tld_list= file.readlines()



def embedded(url_string):
	
			





