# -*- coding: utf-8 -*- 
#���ɸ���MD5�ֵ�

import hashlib

#6λ����
def num6():
	for i in range(100000,999999):
		print str(i) + ',' + md5(i)

#������
def weak_word():
	f = open('dict/weakword.txt',"r")
	line = f.readline()
	while line:
		i = line[:-1]
		print str(i) + ',' + md5(i)
		line=f.readline()
	f.close()

	
	#for i in a:
	#	print str(i) + ',' + md5(i)

def md5(arg):
	return str(hashlib.md5(str(arg)).hexdigest())
	

	

if __name__=="__main__":
	#num6()
	weak_word()