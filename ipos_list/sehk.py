from bs4 import BeautifulSoup
from pandas import DataFrame
import requests

def sehk_ipos(instance):
    response = requests.get("http://www.hkexnews.hk/reports/newlisting/new_listing_announcements.htm")
    soup = BeautifulSoup(response.content,"html.parser")
    s1 = soup.find_all("table", {"class": "table_grey_border ms-rteTable-BlueTable_ENG"})
    s2 = s1[0].find_all('tbody')
    tr = s2[0].find_all('tr')
    header_list = []
    for td in tr[0].find_all('td'):
        header_list.append(td.string)
    header_list.append('Link1')
    header_list.append('Link2')
    sehk_dataframe = DataFrame(columns=header_list)
    pos = 0
    # counter = 0
    for i in range(1, len(tr)):
        temp_list = []
        link_list = []
        for td in tr[i].find_all('td'):
            #         temp_list.append(td.string)
            temp_str = td.find('a')
            if temp_str != None:
                link_list.append('http://www.hkexnews.hk' + temp_str.get('href'))
            temp_list.append(td.string)

        temp_list.extend(link_list)

        try:
            sehk_dataframe.loc[pos] = temp_list
        except:
            temp_list.append(None)
            sehk_dataframe.loc[pos] = temp_list

        pos += 1

    return sehk_dataframe