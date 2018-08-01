from bs4 import BeautifulSoup
import requests
from pandas import DataFrame

def lse_ipos(instance):
    response = requests.get('http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/new-and-recent-issues/new-issues.html')
    soup = BeautifulSoup(response.content,"html.parser")
    lse_scrape = soup.find_all("table", {"class": "table_dati"})
    lse_scrape = lse_scrape[0]
    all_th = lse_scrape.find_all("th")
    table_list = []
    for i in range(len(all_th) - 1):
        for th in all_th[i].find_all("p", {"class": "floatsx linenormal"}):
            table_list.append(th.string)
    lse_dataframe = DataFrame(columns=table_list)
    lse_dataframe['amount raised'] = ''
    pos = 0
    tbody = lse_scrape.find_all("tbody")
    all_tr = tbody[0].find_all("tr")
    for a in range(len(all_tr)):
        temp_list = []
        for i in all_tr[a].find_all("td"):
            temp_list.append(i.string)
        lse_dataframe.loc[pos] = temp_list
        pos += 1

    return lse_dataframe