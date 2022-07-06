# -*- coding: utf-8 -*-
"""
Created on Tue May 10 18:45:02 2022

@author: TalhaSoftware
"""

import requests
from bs4 import BeautifulSoup
import re 
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import itertools
import pandas as pd

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

url = "https://dune.com/queries/350606/667129"

options = Options()
# options.headless = True
browser = webdriver.Firefox()

browser.get(url)

realblacklisted = []
page_number=3

while(page_number < 10):

    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'table_table__fuS_N')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        
    
    
    b = myElem.text.split("\n")
    
    addresses = []
    for i in b:
    
        if(i.startswith("0x")):
            addresses.append(i)
    
    dontwant = []
    for i in range(1,len(addresses),3):
        print(addresses[i])
        dontwant.append(addresses[i])
    
    
    for element in addresses:
        if element not in dontwant:
            realblacklisted.append(element)
    
    browser.find_element_by_css_selector(".table_footer__aB65O > li:nth-child(6) > button:nth-child(1)").click()
    
    

# delay = 15
# try:
#     myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'table_table__fuS_N')))
#     print("Page is ready!")
# except TimeoutException:
#     print("Loading took too much time!")
    

h = myElem.text.split("\n")




