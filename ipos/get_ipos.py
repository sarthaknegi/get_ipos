from selenium import webdriver
from ipos_list import nyse,nasdaq,lse,euronext,sehk,bse,nsei,tyo,tsx

class get_ipos():
    def __init__(self, path):
        """
        :param path: expects the path of the chrome driver.

        """
        try:
            #self.path = path
            self.headless = webdriver.ChromeOptions()
            self.headless.add_argument('--headless')
            self.headless.add_argument('--disable-gpu')
            self.headless_browser = webdriver.Chrome(path, options=self.headless)
        except Exception as e:
            print(e)

    def nyse(self):
        """
        :return: dataframe, containing all the recent ipos

        """
        return nyse.nyse_ipos(self.headless_browser)

    def nasdaq(self):
        """

        :return: dataframe, containing all the recent ipos
        """
        return nasdaq.nasdaq_ipos(self.headless_browser)


    def tyo(self): #tokoyo stock exchange
        """

        :return: dataframe, containig all the recent issues
        """

        return tyo.tyo_ipos(self.headless_browser)


    def lse(self):
        """

        :return: dataframe, containig all the recent issues
        """
        return lse.lse_ipos(self.headless_browser)

    def euronext(self):
        """
        :return:  dataframe, containig all the recent issues
        """
        return euronext.euronext_ipos(self.headless_browser)


    def sehk(self): #stock exchange of hong kong
        """

        :return: dataframe, containig all the recent issues
        """
        return sehk.sehk_ipos(self.headless_browser)


    def  tsx(self): #toronto stock exchange
        """

        :return: dataframe, containig all the recent issues
        """
        return tsx.tsx_ipos(self.headless_browser)


    def bse(self):
        """

        :return: dataframe, containig all the recent issues
        """

        return bse.bse_ipos(self.headless_browser)



    def nsei(self):
        """

        :return: dataframe, containig all the recent issues
        """

        return nsei.nse_ipos(self.headless_browser)

