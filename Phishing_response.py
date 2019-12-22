#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program sends randomly generated data to a fake goverment website.

SMS:
HMRC Have determined that you are eligible for a tax rebate of £228.88. 
Press the link to get started. 
https://gov.uk-auth-c58.com/account
"""

import requests 
import random
import csv

url= 'https://gov.uk-auth-c58.com/account/Finish.php?ssl_id=GfAlwBJ3gtIq17F6jurP3d9sHYPoGJCnYcIvOrz4VhvWpa3IEuyIIIapG0OnJqKICsdqUNvP40MubPcQkLy3uIsbJgysGjajMoJGbfwgfiKq8XhsJPvdyYohfXJWgUf2jZ'

def rand_x_digit_num(x):    
    return random.randint(10**(x-1), 10**x-1)  
      
with open('firstnames.csv', 'r') as filea:
  readera = csv.reader(filea)
  firstnames = list(readera)

with open('surnames.csv', 'r') as fileb:
  readerb = csv.reader(fileb)
  surnames = list(readerb)

for entry in range (100):
    ccname = str(''.join(random.choice(firstnames)+[' ']+random.choice(surnames)).lower())
    ccno = rand_x_digit_num(16)
    ccexp =  str('0')+(str(random.randint(1,9)))+' '+'/'+ ' ' + str(random.randint(20,22))
    secode = random.randint(150,750)
    account = rand_x_digit_num(8)
    sortcode = str('0')+str(random.randint(3,8))+'-'+str(random.randint(3,8))+ str('0')+'-'+str(random.randint(11,55))
    print ('Inserted: ' +ccname,ccno,ccexp,secode,account,sortcode)
    requests.post(url,allow_redirects = False, data ={
        'tes': r'csrfToken,user_id,password,profile:6180403181099740681::Z7PJmvIbwqpEkYXuwErxkhl6/47IiqWuUIG089Fk/n9Rs34jIFTbTGzC3cNDsii8GVso7bwbKSw3KI/uEjS7Ag==',
        'csrfToken': r'60e95235e20c5eed27a06f25a9f99e782833a652\\-1553630837725-185ce4b4a7e1ecf38c2b8b1a',
        'ccname': ccname,
        'ccno': ccno,
        'ccexp': ccexp,
        'secode': secode,
        'account': account,
        'sortcode': sortcode
    })