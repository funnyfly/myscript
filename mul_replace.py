#!/usr/bin/python
#-*-coding: utf-8 -*-
'''
lua文件转python格式
'''
import os

with open('cfg.lua','r') as fs , open('cfg.py','w') as fg:
    line = fs.readline()
    sou_ch = ['[',']','=','-','S95']
    gol_ch = ['','',':','#','clientStorageChangeInfoData']
    while line:
        for i in range(len(sou_ch)):
            line = line.replace(sou_ch[i],gol_ch[i])
        fg.write(line)
        line = fs.readline()
