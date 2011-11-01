# -*- coding: utf-8 -*-
import hashlib
import base64
import sys
import binascii

def ascii_ord(arg):
    a = ''
    for s in arg:
        a += str(ord(s)) + ' '
    return a
    
def run(arg):
    print '原始值    :' + arg
    print 'URL    :' + arg
    print 'ASCII  :' + ascii_ord(arg) 
    print '16进制   :' + '0x' + binascii.b2a_hex(arg).upper()
    print 'MD5-16 :' + hashlib.md5(arg).hexdigest()[8:-8]
    print 'MD5-32 :' + hashlib.md5(arg).hexdigest()
    print 'sha1   :' + hashlib.sha1(arg).hexdigest()
    print 'sha224 :' + hashlib.sha224(arg).hexdigest()
    print 'sha256 :' + hashlib.sha256(arg).hexdigest()
    print 'sha384 :' + hashlib.sha384(arg).hexdigest()
    print 'sha512 :' + hashlib.sha512(arg).hexdigest()
    print 'Base64 :' + base64.b64encode(arg)
    
    
if __name__ == '__main__':
    arg = 'admins'#sys.argv[1]
    run(arg)