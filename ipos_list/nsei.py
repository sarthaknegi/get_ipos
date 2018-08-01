from time import sleep
from bs4 import BeautifulSoup
from pandas import DataFrame

def nse_ipos(instance):
    instance.get('https://www.nseindia.com/products/content/equities/ipos/homepage_ipo.htm')
    sleep(5)
    source = instance.page_source

    nse_soup = BeautifulSoup(source)

    nse_div = nse_soup.find_all('div', attrs={"class": "tabular-data-historic"})

    sleep(5)
    nse_tbody = nse_div[0].find_all('tbody')

    head = nse_tbody[0].find_all('tr', attrs={'class': 'alt'})
    table_headers = []
    for data in head[0].find_all('td'):
        table_headers.append(data.string)

    table_headers.append('Symbol')
    #     table_headers.append('Issue Type')

    nse_dataframe = DataFrame(columns=table_headers)
    tr = nse_tbody[0].find_all('tr')

    pos = 0
    for i in range(1, len(tr)):
        temp_list = []
        td = tr[i].find_all('td')

        for data in td:
            temp_list.append(data.string)

        link = td[0].find_all('a')
        if link:
            link = link[0].get('href')
            instance.get('https://www.nseindia.com' + link)
            sleep(5)
            extra_data = instance.page_source
            extra_soup = BeautifulSoup(extra_data)

            extra_div = extra_soup.find_all("div", attrs={"id": "ipo_mid"})
            extra_table = extra_div[0].find_all('table')

            extra_tbody = extra_table[0].find_all('tbody')
            extra_tr = extra_tbody[0].find_all('tr')

            for j in range(1, len(extra_tr)):
                td = extra_tr[j].find_all('td')
                temp_str = td[0].string
                try:
                    temp_str = temp_str.replace(' ', '')
                except:
                    pass
                if temp_str == 'Symbol':
                    temp_list.append(td[1].string)
                    break

        if len(temp_list) >= 1:
            try:
                nse_dataframe.loc[pos] = temp_list
                pos += 1
            except:
                pass


    return nse_dataframe