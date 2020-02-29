import requests as rq 
import lxml
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from tabulate import tabulate

def getSoup(url, parser='html.parser'):
    url2 = bs(url.text, parser)
    return url2

def tableDataText(table):       
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows


def getTable(year, ec, gender):
    source = rq.get('http://trackfield.brinkster.net/More.asp?Year=%s&EventCode=%s&Gender=%s&P=T'%(year, ec, gender))
    source = getSoup(source)
    table = source.find('table')
    return tableDataText(table)

# df = pd.DataFrame(t2[2:-2])

def getRange(start, stop, ec, gender):
    df = pd.DataFrame(getTable(start, ec, gender)[2:-2])
    print('Got %s.' %(start))
    # for i in range(start + 1, stop + 1):
    i = start + 1
    while i <= stop:
        try:
            df2 = pd.DataFrame(getTable(str(i), ec, gender)[2:-2])
            for col in df2:
                if col == '7':
                    col = col + i
                else:
                    pass                
            df = df.append(df2)
            print('Got %s.' %(i))
            time.sleep(0.1)
        except Exception as e:
            i -= 1
            print('Connection dropped (%s), retrying...'%e)
        i += 1
    df.columns = ['ID', 'Name', 'Country', 'Time', 'TrucChelou', 'TrucChelou2', 'City', 'Date']
    return df


ret = getRange(2010,2019,'WF4','W')
# print(ret[ret.Time == ret.Time.min()])

# top25 = pd.DataFrame()
# for i in range(0,25):
#     top25 = top25.append(ret[ret.Time == ret.Time.min()])
#     ret.drop(ret[ret.Time == ret.Time.max()])
ret.sort_values(by='Time', inplace=True)
top25 = pd.DataFrame(ret[:25])
top25.reset_index(inplace=True)
top25.drop('ID', axis=1, inplace=True)
top25.drop('index', axis=1, inplace=True)
print(top25)
top25.to_csv(r'/home/samuel/Workspace/Playgrounds/Python-Playground/Corbeilles/Scraping/Brief/top25.csv', index = False)