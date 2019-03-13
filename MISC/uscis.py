#!/usr/bin/python3

import pandas as pd
import bs4, urllib
import datetime
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://egov.uscis.gov/casestatus/mycasestatus.do{hahahahahahaah}"    #"https://egov.uscis.gov/casestatus/landing.do"

df = pd.DataFrame(columns=['Case Number','Status'])
casenumberfront = "YSC199010"
for i in range("enter your desired number of iterations"):
    post_params = {"appReceiptNum": casenumberfront+str(i).zfill(4)}
    param = urllib.parse.urlencode(post_params).encode("utf-8")
    uClient = uReq(my_url,param)
    page = uClient.read()
    uClient.close()
    page_soup = soup(page,"html.parser")
    # print(type(page))
    # print(type(page_soup))

    answer = page_soup.findAll("div",{"class":"current-status-sec"})
    # print(type(str(answer[0])))
    if "I-765" in str(page):
        if "Case Was Received" in str(answer[0]):
            df = df.append({"Case Number":casenumberfront+str(i).zfill(4),"Status":"Not Processed"},ignore_index=True)
            print("case was received")
        else:
            df = df.append({'Case Number':casenumberfront+str(i).zfill(4),"Status":"Processed"},ignore_index=True)
    print(i/10000)
print(df)
df.to_csv(str(datetime.datetime.now()))

