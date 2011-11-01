# -*- coding: utf-8 -*-

from sqlalchemy import *
from datetime import datetime

metadata = MetaData('sqlite:///../db/md5.sqlite')
metadata.bind.echo = True

num6 = Table(
    't_md5_num6', metadata,
    Column('id', Integer, primary_key=True),
    Column('key', String(12), unique=True, nullable=False),
    Column('md5', String(16), unique=True, nullable=False))

def create():
    metadata.create_all()
    
def insert():
    stmt = num6.insert()
    stmt.execute(id='2', key='secre1t',md5='Rick C1opeland')

def query():
    stmt = num6.select()
    result = stmt.execute().fetchall()
    for row in result:
        print row

if __name__ == '__main__':
    #create()
    #insert()
    query()
    
