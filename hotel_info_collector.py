from selenium import webdriver


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
