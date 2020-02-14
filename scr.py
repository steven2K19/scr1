import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd


def scr(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    table = soup.find('div', id='table_div')
    row = table.find_all('div')
    l=[]
    for x in row:
        span = x.find_all('span')
        r=[x.text for x in span]
        l.append(r)
    l = [x for x in l if x != []]
    lens=[]
    for num in range(0,30,1):
        lens.append(len(l[num]))
    cols=[]
    for num in range(1, max(lens)+1,1):
        cols.append('col'+str(num))
    df=pd.DataFrame(l,columns=cols)
    df= df[['col1','col2','col5','col7','col9','col11','col13','col15']]
    return df
  

url = "https://www.opera-arias.com/arias/"
df = scr(url)

for num in range (2,99,1):
    url2= "https://www.opera-arias.com/arias/&page={0}#x".format(num)
    df2=scr(url2)
    df=df.append(df2)
