# -*- coding: utf-8 -*- 

#读字典文件
def dict_read(file):
    lines = []
    f = open(file,"r")
    
    line = str(f.readline())
    lines.append(line.split(','))
    while line:
        line = f.readline()
        lines.append(line.split(','))
    f.close()
    return lines