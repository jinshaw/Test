# -*- coding: UTF-8 -*-
from selenium import webdriver

user_file=open('account.txt','r')
lines=user_file.readlines()
user_file.close()

for i in lines:
     username=i.split(',')[0]
     password=i.split(',')[1]
     print (username,password)