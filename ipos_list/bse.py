import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


def bse_ipos(instance):
    bse_page = requests.get('http://www.bseindia.com/markets/PublicIssues/IPOIssues_new.aspx?id=1&Type=p')
    bse_soup = BeautifulSoup(bse_page.content, "lxml")

    bse_data = bse_soup.find_all('table', class_='tablesorter')

    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []

    tbody = bse_data[0].find_all('tbody')

    for rows in tbody[0].find_all('tr'):
        cells = rows.find_all('td')
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))

    bse_data = DataFrame()
    bse_data['Security'] = A
    bse_data['Start Date'] = B
    bse_data['End Date'] = C
    bse_data['Offer Price'] = D
    bse_data['Face Value'] = E
    bse_data['Type of Issues'] = F
    bse_data['Issue Status'] = G

    return bse_data

