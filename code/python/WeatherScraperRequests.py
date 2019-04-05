from bs4 import BeautifulSoup
import requests
import time

class WeatherScraper(object):
    def __init__(self,):
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
        self.urls = []

    def createUrls(self):
        for x in range(58):
            rootUrl = 'https://www.weatherforyou.com/reports/index.php?pands='
            finalUrl = 'https://www.weatherforyou.com/reports/index.php?pands='
            countyFormatted = self.counties[x].replace(' ', '+')

            finalUrl += countyFormatted
            finalUrl += '+county%2Ccalifornia'
            self.urls.append(finalUrl)

    def weatherScrape(self):
        for url in self.urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            Temp = soup.find('span', class_ = 'Temp')
            weatherTemp = Temp.text
            weatherTemp = weatherTemp[:-2]

            weatherValues = soup.findAll('span', class_ = 'Value')

            Humid = weatherValues[0]
            Wind = weatherValues[1]

            weatherHumid = Humid.text
            weatherHumid = self.filterHumid(weatherHumid)

            weatherWind = Wind.text
            weatherWind = self.filterWind(weatherWind)

            weatherTemp = int(weatherTemp)
            weatherHumid = int(weatherHumid)
            weatherWind = int(weatherWind)

            self.temps.append(weatherTemp)
            self.humidity.append(weatherHumid)
            self.winds.append(weatherWind)

            print('Done scraping URL: ' + url)

    def filterWind(self, text):
        if(text == 'N/A'):
            return 0;
        weatherWindSplit = [int(s) for s in text.split() if s.isdigit()]

        if (len(weatherWindSplit) > 0):
            weatherWind = weatherWindSplit[0]
        else:
            weatherWind = 0

        return weatherWind

    def filterHumid(self, text):
        if(text == 'N/A'):
            return 0;
        else:
            return text[:-1]

    def getCounties(self):
        return self.counties

    def getTemps(self):
        return self.temps

    def getHumidity(self):
        return self.humidity

    def getWinds(self):
        return self.winds
