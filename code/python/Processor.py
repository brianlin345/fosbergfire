import WeatherScraperRequests
import Region
import CSVWriter

class Processor(object):
    def __init__(self):
        self.Writer = CSVWriter.CSVWriter()
        self.Scraper = WeatherScraperRequests.WeatherScraper()
        self.Formatted = []
        self.CalculatedData = []
        self.urls = ["https://www.acgov.org/", "https://www.alpinecountyca.gov/", "http://www.amadorgov.org/",
                     "https://www.buttecounty.net/", "http://calaverasgov.us/", "https://www.countyofcolusa.org/",
                     "http://www.co.contra-costa.ca.us/", "http://www.co.del-norte.ca.us/", "https://www.edcgov.us/",
                     "http://www.co.fresno.ca.us/", "https://www.countyofglenn.net/", "https://humboldtgov.org/",
                     "http://www.co.imperial.ca.us/", "http://www.inyocounty.us/", "http://www.kerncounty.com/",
                     "http://www.countyofkings.com/", "http://www.co.lake.ca.us/", "http://www.co.lassen.ca.us/",
                     "http://www.lacounty.gov/", "http://www.madera-county.com/", "http://www.marincounty.org/",
                     "http://www.mariposacounty.org/", "http://www.mendocinocounty.org/", "http://www.co.merced.ca.us/",
                     "http://www.co.modoc.ca.us/", "http://www.monocounty.ca.gov/", "http://www.co.monterey.ca.us/",
                     "http://www.countyofnapa.org/", "https://www.mynevadacounty.com/", "http://www.ocgov.com/",
                     "http://www.placer.ca.gov/", "http://www.countyofplumas.com/", "http://www.countyofriverside.us/",
                     "http://www.saccounty.net/", "http://www.san-benito.ca.us/", "http://www.sbcounty.gov/default.asp",
                     "http://www.co.san-diego.ca.us/", "http://sfgov.org/", "http://www.co.san-joaquin.ca.us/",
                     "http://www.slocounty.ca.gov/", "http://www.co.sanmateo.ca.us/", "http://www.countyofsb.org/",
                     "http://www.sccgov.org/", "http://www.co.santa-cruz.ca.us/", "http://www.co.shasta.ca.us/",
                     "http://www.sierracounty.ca.gov/", "http://www.co.siskiyou.ca.us/", "http://www.co.solano.ca.us/",
                     "http://www.sonoma-county.org/", "http://www.co.stanislaus.ca.us/", "http://www.co.sutter.ca.us/",
                     "http://www.co.tehama.ca.us/", "http://www.trinitycounty.org/", "http://www.co.tulare.ca.us/",
                     "http://www.tuolumnecounty.ca.gov/", "http://www.countyofventura.org/","http://www.yolocounty.org/",
                     "http://www.co.yuba.ca.us/"]

    def scrapeWeather(self):
        self.Scraper.createUrls()
        self.Scraper.weatherScrape()
        self.counties = self.Scraper.getCounties()
        self.temps = self.Scraper.getTemps()
        self.humidity = self.Scraper.getHumidity()
        self.winds = self.Scraper.getWinds()

    def generateData(self):
        for i in range(58):
            tempRegion = Region.Region(self.temps[i], self.humidity[i], self.winds[i])
            tempRegion.castVariables()
            tempRegion.calcEquilMoisture()
            tempRegion.calcMoistureDampening()
            self.CalculatedData.append(tempRegion.calcFinal())

    def generateFormatted(self):
        for i in range(58):
            temp = [self.counties[i], self.CalculatedData[i], self.temps[i], self.humidity[i], self.winds[i], self.urls[i]]
            self.Formatted.append(temp)

    def writeFile(self):
        self.Writer.writeLines(self.Formatted)