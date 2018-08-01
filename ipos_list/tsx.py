from bs4 import BeautifulSoup
from pandas import DataFrame
from time import sleep



def redundant(tmx_soup):
    tmx_table = tmx_soup.find_all('table', attrs={'class': 'sizeable'})

    header = tmx_table[0].find_all('thead')
    tmx_tr = header[0].find_all('tr')
    header_list = []
    for th in tmx_tr[0].find_all('th'):
        header_list.append(th.string)


    tmx_dataframe = DataFrame(columns=header_list)
    tmx_body = tmx_table[0].find_all('tbody')
    pos = 0
    for tr in tmx_body[0].find_all('tr'):
        temp_list = []
        for td in tr.find_all('td'):
            links = td.find('a')
            if links is None:
                temp_str = tr.find('td', attrs={'class' :'nowrap'})
                temp_str = temp_str.text
                temp_list.append(temp_str[4:])
            else:
                temp_list.append(links.text)

        tmx_dataframe.loc[pos] = temp_list
        pos += 1

    return tmx_dataframe


def tsx_ipos(instance):
    instance.get('https://www.tsx.com/listings/listing-with-us/listed-company-directory?GetPage=ListedCompaniesViewPage&ListedCompanyTab=RecentlyListed&Market=V&Language=en')

    instance.find_element_by_id('exchange-toggle').click()
    sleep(10)
    tsx_soup = BeautifulSoup(instance.page_source)
    tsx_dataframe = redundant(tsx_soup)

    return tsx_dataframe