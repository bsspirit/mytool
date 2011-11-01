# -*- coding: utf-8 -*- 
from sqlalchemy.orm import *

class User(object): pass
class Group(object): pass
class Permission(object): pass

mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)