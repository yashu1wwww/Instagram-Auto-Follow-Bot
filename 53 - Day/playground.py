import requests
from bs4 import BeautifulSoup
import lxml


#######################################################################################################################
#
#           Variables
#
#######################################################################################################################
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

CHROME_DRIVER_PATH = "c:/Development/chromedriver.exe"
GOOGLE_FORM_URL = "https://forms.gle/YHAoNLEa182pj4Mt6"


#######################################################################################################################
#
#           Scraping
#
#######################################################################################################################
class Scraping:
    def __init__(self, url, header):
        self.ZILLOW_URL = url
        self.HEADER = header
        self.response = requests.get(url=self.ZILLOW_URL, headers=self.HEADER)
        self.data = self.response.text

        self.soup = BeautifulSoup(self.data, "lxml")
        self.prices_list = None
        self.address_list = None
        self.link_list = None
        self.data = None

    def price(self):
        price_list = self.soup.select(selector="ul.List-c11n-8-70-0__sc-1smrmqp-0.srp__sc-1psn8tk-0.gDSXAC.photo-cards.with_constellation li div.StyledPropertyCardDataArea-c11n-8-70-0__sc-yipmu-0.jSVWjf span")
        self.prices_list = [price.getText() for price in price_list]

    def address(self):
        all_address = self.soup.select(selector="ul.List-c11n-8-70-0__sc-1smrmqp-0.srp__sc-1psn8tk-0.gDSXAC.photo-cards.with_constellation li address")
        self.address_list = [address.getText() for address in all_address]

    def link(self):
        all_links = self.soup.select(selector="ul.List-c11n-8-70-0__sc-1smrmqp-0.srp__sc-1psn8tk-0.gDSXAC.photo-cards.with_constellation li div.jRqzri a")
        self.link_list = [link.get("href") for link in all_links]

    def card(self):
        self.data = []

        for i in range(len(self.prices_list)):
            if "http" not in self.link_list[i]:
                self.link_list[i] = "https://www.zillow.com" + self.link_list[i]

            self.data.append({
                "price": self.prices_list[i],
                "address": self.address_list[i],
                "link": self.link_list[i]
            })

        return self.data


# zillow = Scraping(url=ZILLOW_URL, header=HEADER)
#
# zillow.price()
# zillow.address()
# zillow.link()
# data = zillow.card()
#
# print(data)


#######################################################################################################################
#
#           BOT
#
#######################################################################################################################


