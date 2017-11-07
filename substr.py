#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
打印字符串的全量子串
'''
st = 'abcde'

def sub_str(st):
    l = []
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            l.append(st[i:j])
    print l
if __name__ == "__main__":
    sub_str(st)
