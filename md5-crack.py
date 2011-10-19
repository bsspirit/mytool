# -*- coding: utf-8 -*- 
# MD5破解工具
# 作者: x140m1ng
# 邮箱: <lininruc[at]gmail[dot]com>
# 博客: http://hi.baidu.com/ruclin
# 将 md5拿到网上去搜，然后返回正确的值。

import sys , re , urllib, urllib2,string
from urllib2 import Request , urlopen , URLError , HTTPError

#md5("admin") = 21232f297a57a5a743894a0e4a801fc3

def print_usage():
    print "md5crack.py version:0.1"
    print "Author:x140m1ng"
    print "Example: python md5crack.py 21232f297a57a5a743894a0e4a801fc3"
    return

def print_banner():
    return

def main():
    print_banner()
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    else:
        hash=sys.argv[1]

        #site3:md5.hashcracking.com [get]
        request=urllib2.Request("http://md5.hashcracking.com/search.php?md5="+hash)
        response=urllib2.urlopen(request)
        print "[+] md5.hashcracking.com:"+response.read()[49:]
       
	    """
        #site6:http://md5.drasen.net/search.php?query=
		try:
			request=urllib2.Request("http://md5.drasen.net/search.php?query="+hash)
			response=urllib2.urlopen(request)
			link = re.findall(r'Plain:[^<>]*', response.read())
			print "[+] md5.drasen.net/search.php:"+link[0][7:]
		except:
			print 'error'
		"""	
       """
        #site8:http://md5-db.de/${HASH}.html
        request=urllib2.Request("http://md5-db.de/"+hash+".html")
        response=urllib2.urlopen(request)
        link = re.findall(r'<li>[^<>]*', response.read())
        print "[+] md5-db.de/:"+link[0][4:]

        #site11:http://victorov.su/md5/?md5e=&md5d=21232f297a57a5a743894a0e4a801fc3
        request=urllib2.Request("http://victorov.su/md5/?md5e=&md5d="+hash)
        response=urllib2.urlopen(request)
        link = re.findall(r'<b>[^<>]*', response.read())
        print "[+] victorov.su/md5/:"+link[0][3:]
       
       """
       
if __name__=="__main__":
    main()