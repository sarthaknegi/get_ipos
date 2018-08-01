import requests
from bs4 import BeautifulSoup
import datetime
from pandas import DataFrame


def euronext_ipos(instance):
    response = requests.get('https://www.euronext.com/en/welcome?quicktabs_25=1#quicktabs-25')
    soup = response.content
    euronext_soup = BeautifulSoup(soup,"html.parser")
    euronext_s1 = euronext_soup.find_all("div", {"id": "quicktabs_tabpage_25_1"})
    euronext_s2 = euronext_s1[0].find_all("thead")
    euronext_s3 = euronext_s2[0].find_all("th")
    now = datetime.date.today()
    euronext_temp_list = []
    for i in range(len(euronext_s3)):
        euronext_temp_str = str(euronext_s3[i].text)
        euronext_temp_list.append(euronext_temp_str.strip())
    euronext_df = DataFrame(columns=euronext_temp_list)
    euronext_df['Ticker'] = ''
    euronext_df['Subsector'] = ''
    euronext_df['Issue Type'] = ''
    euronext_s4 = euronext_s1[0].find_all("tbody")
    euronext_s5 = euronext_s4[0].find_all("tr")
    #euronext_s6 = euronext_s5[0].find_all("td")
    euronext_pos = 0
    for euronext_b in range(len(euronext_s5)):
        euronext_final = []
        for euronext_a in euronext_s5[euronext_b].find_all("span", {"class": "date-display-single"}):
            euronext_final.append(euronext_a.text)
        for euronext_a in euronext_s5[euronext_b].find_all("a"):
            euronext_final.append(euronext_a.text)
        for euronext_a in euronext_s5[euronext_b].find_all("td", {
            "class": "views-field views-field-field-iponi-isin-code-value"}):
            euronext_final.append(euronext_a.text)
        for euronext_a in euronext_s5[euronext_b].find_all("td", {"class": "views-field views-field-tid"}):
            euronext_final.append(euronext_a.text)
        for euronext_a in euronext_s5[euronext_b].find_all("td", {"class": "views-field views-field-tid-1"}):
            euronext_final.append(euronext_a.text)
        for euronext_a in euronext_s5[euronext_b].find_all("a"):
            euronext_l1 = euronext_a.get('href')
            euronext_l2 = "https://www.euronext.com" + euronext_l1
            euronext_r1 = requests.get(euronext_l2)
            euronext_soup1 = BeautifulSoup(euronext_r1.content)
            euronext_s10 = euronext_soup1.find_all("div", {"class": "if-block"})
            euronext_s11 = euronext_s10[0].find_all("div")
            l = len(euronext_s11)
            euronext_final.append((euronext_s11[l - 1].find_all('strong'))[0].string)
            euronext_final.append((euronext_s11[l - 3].find_all('strong'))[0].string)
            # Now going for Issue type
            euro_issue = euronext_soup1.find_all("div", {"class": "column right"})
            inside_euro_issue = euro_issue[0].find_all("div", {"class": "if-block"})
            divs_inside = inside_euro_issue[0].find_all("div")
            l = len(divs_inside)

            euronext_final.append(
                (divs_inside[1].find_all('strong'))[0].string)  # If there is a error on this line check the site
        euronext_df.loc[euronext_pos] = euronext_final
        euronext_pos += 1

    return euronext_df
