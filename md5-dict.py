# -*- coding: utf-8 -*- 
#���ɸ���MD5�ֵ�

import hashlib

#6λ����
def num6():
	for i in range(100000,999999):
		print str(i) + ',' + md5(i)

def md5(arg):
	return str(hashlib.md5(str(arg)).hexdigest())

if __name__=="__main__":
	num6()