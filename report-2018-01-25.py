import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import pdb
import datetime
#pdb.set_trace() - python step by step debugger command
print datetime.datetime.now()
print "Finviz Overview Start"
url = "https://finviz.com/screener.ashx?v=152&c=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
firstcount = soup.find_all('option')
lastnum = len(firstcount) - 1
lastpagenum = firstcount[lastnum].attrs['value']
currentpage = int(lastpagenum)

alldata = []
templist = []
# Overview = 111, Valuation = 121, Financial = 161, Ownership = 131, Performance = 141
#pagesarray = [111,121,161,131,141]
titleslist = soup.find_all('td',{"class" : "table-top"})
titleslisttickerid = soup.find_all('td',{"class" : "table-top-s"})
titleticker = titleslisttickerid[0].text
titlesarray = []
for title in titleslist:
    titlesarray.append(title.text)

titlesarray.insert(1,titleticker)
i = 0

while(currentpage > 0):
    i += 1
    print str(i) + " page(s) done"
    secondurl = "https://finviz.com/screener.ashx?v=152&c=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68" + "&r=" + str(currentpage)
    secondresponse = requests.get(secondurl)
    secondhtml = secondresponse.content
    secondsoup = BeautifulSoup(secondhtml, "html.parser")
    stockdata = secondsoup.find_all('a', {"class" : "screener-link"})
    stockticker = secondsoup.find_all('a', {"class" : "screener-link-primary"})
    datalength = len(stockdata)
    #tickerdatalength = len(stockticker)

    j=0
    m=0
    while(j < datalength):
        templist = [stockdata[j+k].text for k in range(0, 68)]
        templist.insert(1, stockticker[m].text)
        alldata.append(templist)
        templist = []
        j += 68
        m += 1
    currentpage -= 20

with open('stockoverview.csv', 'wb') as csvfile:
    overview = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=titlesarray)
    overview.writeheader()

    for stock in alldata:
        df = dict()
        for i in range(0,69):
            df[titlesarray[i]] = stock[i]
        overview.writerow(df)

print datetime.datetime.now()
print "Finviz Overview Completed"
