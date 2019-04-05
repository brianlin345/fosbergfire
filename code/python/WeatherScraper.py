from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class WeatherScraper(object):
    def __init__(self,):
        self.driver = webdriver.Chrome('C:/Users/brian/GoogleDriver/chromedriver.exe')
        self.driver.get("http://google.com")
        self.counties = ["Alameda", "Alpine", "Amador", "Butte", "Calaveras", "Colusa",
            "Contra Costa", "Del Norte", "El Dorado", "Fresno", "Glenn",
            "Humboldt", "Imperial", "Inyo", "Kern", "Kings", "Lake", "Lassen",
            "Los Angeles", "Madera", "Marin", "Mariposa", "Mendocino", "Merced", "Modoc",
            "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas",
            "Riverside", "Sacramento", "San Benito", "San Bernardino", "San Diego",
            "San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
            "Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Sierra",
            "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Sutter", "Tehama", "Trinity",
            "Tulare", "Tuolumne", "Ventura", "Yolo", "Yuba"]
        self.temps = []
        self.humidity = []
        self.winds = []

    def weatherScrapeController(self):
        for x in range(58):
            self.searchItem(x)
            self.scrapeTemps(x)
            self.scrapeHumidity(x)
            self.scrapeWind(x)
            time.sleep(1)
        self.driver.close()


    def searchItem(self, index):
        searchElem = self.driver.find_element_by_css_selector("#lst-ib")
        searchElem.send_keys(self.counties[index] + " county weather")
        searchElem.send_keys(Keys.ENTER)


    def scrapeTemps(self, index):
        elem = self.driver.find_element_by_css_selector("#wob_tm")
        self.temps.append(elem.text)
        searchElem = self.driver.find_element_by_css_selector("#lst-ib")
        searchElem.clear()


    def scrapeHumidity(self, index):
        elem = self.driver.find_element_by_css_selector("#wob_hm")
        tempHumidity = elem.text
        removedHumidity = tempHumidity.replace("%", "")
        self.humidity.append(removedHumidity)
        searchElem = self.driver.find_element_by_css_selector("#lst-ib")
        searchElem.clear()

    def scrapeWind(self, index):
        elem = self.driver.find_element_by_css_selector("#wob_ws")
        tempWind = elem.text
        removedWind = tempWind.replace("mph", "")
        self.winds.append(removedWind)
        searchElem = self.driver.find_element_by_css_selector("#lst-ib")
        searchElem.clear()


    def getCounties(self):
        return self.counties

    def getTemps(self):
        return self.temps

    def getHumidity(self):
        return self.humidity

    def getWinds(self):
        return self.winds

