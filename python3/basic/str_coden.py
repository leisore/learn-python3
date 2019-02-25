#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'Tomcat'
print(name.encode())
print(name.encode('ascii'))
print(name.encode('utf-8'))

name2 = "唐纳德"
print(name2.encode())
#print(name2.encode('ascii'))
print(name2.encode('utf-8'))
    
name2UTF8 = name2.encode('utf-8')
name2GB2312 = name2.encode('GB2312')
print(name2UTF8)
print(name2GB2312)

# 文
print(ord('文'))
print(chr(25991))

