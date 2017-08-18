#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import  hashlib
x=hashlib.md5()
words='D:\\software\\system\\Pidora-2014-R3\\Pidora-2014-R3.img'
f=open(words,'rb')
while words!='':
    words=f.read(1024000)
    x.update(words)
print x.hexdigest()
