# -*- coding: utf-8 -*-
from sqlalchemy import *
from datetime import datetime

metadata = MetaData('sqlite:///../db/md5.sqlite')
#metadata.bind.echo = True

num6 = Table(
    't_md5_num6', metadata,
    Column('key', String(12), unique=True, nullable=False, primary_key=True),
    Column('md5', String(16), unique=True, nullable=False))

def create():
    metadata.create_all()
    
def insert(k,v):
    stmt = num6.insert()
    stmt.execute(key=k,md5=v)

def query():
    stmt = num6.select()
    result = stmt.execute().fetchall()
    for row in result:
        print row

def queryKey(k):
    stmt = num6.select(k)
    row = stmt.execute().fetchone()
    print row

if __name__ == '__main__':
#    create()
 #   insert()
  #  query()
    queryKey('100001')    
