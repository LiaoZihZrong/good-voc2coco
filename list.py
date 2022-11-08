# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 21:53:11 2021

@author: liaozz
"""
import os
path = "/home/nvidia1070/Downloads/new-head/okxml/"

# 獲取該目錄下所有檔案，存入列表中
f = os.listdir(path)

for i in range(len(f)):
    if "xml" in f[i]:
        open_txt = open('output003.txt', 'a')
        #write_in=str(path)+str(f[i])+"\n"
        write_in=str(f[i])+"\n"
        print(write_in)
        open_txt.write(str(write_in))
        open_txt.close()

print("OK")
