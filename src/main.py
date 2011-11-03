# -*- coding: utf-8 -*-
import md5_db as db
import md5_rdict as rdict

if __name__ == '__main__':
    db.create()
    lines = rdict.dict_read('../gen/md5/num6.txt')
    for obj in lines:
        db.insert(obj[0], obj[1])