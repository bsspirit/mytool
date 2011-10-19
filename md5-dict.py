# -*- coding: utf-8 -*- 
#���ɸ���MD5�ֵ�

import hashlib
import zipfile

#6λ����
def num6():
	for i in range(100000,999999):
		print str(i) + ',' + md5(i)

#�ı�
def file_read(file):
	f = open(file,"r")
	line = f.readline()
	while line:
		if line != '':
			i = line.rstrip()
			print str(i) + ',' + md5(i)
		line=f.readline()
	f.close()

#ѹ��
def zip_read(file):
	z = zipfile.ZipFile(file,'r')
	for name in z.namelist():
		f = z.open(name,'r')	
		line = f.readline()
		while line:
			if line != '':
				i = line.lower().rstrip()
				print str(i) + ',' + md5(i)
			line=f.readline()
		f.close()

def md5(arg):
	return str(hashlib.md5(str(arg)).hexdigest())

if __name__=="__main__":
	#num6()
	#zip_read('dict/weakword.zip')
	zip_read('dict/name_pinyin.zip')
	#file_read('dict/name_brithday.txt')
