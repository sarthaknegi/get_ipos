from bs4 import BeautifulSoup
import pandas as pd


def nyse_ipos(instance):
    instance.get('https://www.nyse.com/ipo-center/recent-ipo')

    nyse_data = instance.page_source

    nyse_soup = BeautifulSoup(nyse_data)
    nyse_soup_data = nyse_soup.find_all('table', attrs={'class':'table-condensed'})
    nyse_soup_data = nyse_soup_data[0]

    table_headers = nyse_soup_data.find_all('thead')

    table_headers_list = []
    for th in table_headers[0].find_all('th'):
        table_headers_list.append(th.string)

    pos = 0
    nyse_dataframe = pd.DataFrame(columns=table_headers_list)

    nyse_ipo_table = nyse_soup_data.find_all('tbody')

    for rows in nyse_ipo_table[0].find_all('tr'):
        level = 0
        temp_list = []
        cells = rows.find_all('td')  # finding all the td's inside the tr

        while level < len(table_headers_list):  # done this to avoid hardcoding column names
            temp_list.append(cells[level].find(text=True))
            level += 1

        nyse_dataframe.loc[pos] = temp_list  # adding the data to the dataframe
        pos += 1

    return nyse_dataframe
