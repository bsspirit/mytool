# -*- coding: utf-8 -*- 

import hashlib

def main(arg):
	m = hashlib.md5(arg)
	print m.hexdigest()
       
if __name__=="__main__":
    main('1987654')