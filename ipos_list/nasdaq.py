from bs4 import BeautifulSoup
import pandas as pd
import requests

def nasdaq_ipos(instance):
    nasdaq_url = requests.get('http://www.nasdaq.com/markets/ipos/activity.aspx?tab=upcoming')  # opening the url
    nasdaq_soup = BeautifulSoup(nasdaq_url.content, "html.parser")

    header = nasdaq_soup.find_all('div', class_="ipo-pagination-div")  # getting the title of the table
    # the header definig the table contents
    title = header[0].find_all('h4')[0].string

    nasdaq_data = nasdaq_soup.find_all('div', class_="genTable")  # getting the div where the table is stored
    nasdaq_data = nasdaq_data[0].find_all('table')  # now from inside the div taking the table out

    table_headers = nasdaq_data[0].find_all('thead')  # thead stores all the headers

    table_headers_list = []
    for th in table_headers[0].find_all('th'):
        table_headers_list.append(th.string)

    nasdaq_dataframe = pd.DataFrame(columns=table_headers_list)  # creating the dataframe to store the data
    nasdaq_dataframe.name = title

    pos = 0
    nasdaq_data_tbody = nasdaq_data[0].find_all('tbody')  # tbody is where the row data is stored
    for rows in nasdaq_data_tbody[0].find_all('tr'):
        level = 0
        temp_list = []
        cells = rows.find_all('td')  # finding all the td's inside the tr

        while level < len(table_headers_list):  # done this to avoid hardcoding column names
            temp_list.append(cells[level].find(text=True))
            level += 1

        nasdaq_dataframe.loc[pos] = temp_list  # adding the data to the dataframe
        pos += 1

    return nasdaq_dataframe