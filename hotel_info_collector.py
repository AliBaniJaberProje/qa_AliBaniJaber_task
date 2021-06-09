

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HotelInfoCollector:
    CHROME_DRIVER_PATH = './chromedriver_linux64/chromedriver'
    XPATH_HOTEL_REVIEW = '//*[@id="js--hp-gallery-scorecard"]/a/div/div[2]/div[1]'
    XPATH_HOTEL_NAME = '//*[@id="hp_hotel_name"]'

    def __init__(self):
        self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH)

    def get_hotel_info(self, url):
        hotel_name = None
        hotel_review = None
        try:
            self.driver.get(url)
            hotel_name = self.driver.find_element_by_xpath(self.XPATH_HOTEL_NAME).text
            hotel_review = self.driver.find_element_by_xpath(self.XPATH_HOTEL_REVIEW).text
        except:
            pass
        return [hotel_name, hotel_review]

    def __del__(self):
        self.driver.close()


# selenium_driver=SeleniumDriver()
#
# print(selenium_driver.get_current_name_and_review("https://www.booking.com/hotel/nl/valkvianen.nl.html?label=gen173nr-1DCAsoqQFCCnZhbGt2aWFuZW5IM1gEaKkBiAEBmAEcuAEYyAEM2AED6AEB-AEDiAIBqAIEuALb4qH3BcACAdICJGUzNTA3ZGI3LWQ4N2MtNGZmMi04ZGQ4LWU2ZmYyNjhmYWZiM9gCBOACAQ;sid=e133275a8e06c379a7996d8d10866dca;checkin=2020-06-16&checkout=2020-06-17&dist=0&group_adults=2&keep_landing=1&sb_price_type=total&type=total&#tab-main"))
