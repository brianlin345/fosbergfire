import Processor
import subprocess

from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

jsonKeyfile = 'C:/HTML Files/FosbergSite/FosbergFire-bba334df2ba6.json'


credentials = ServiceAccountCredentials.from_json_keyfile_name(filename=jsonKeyfile)


process = Processor.Processor()
process.scrapeWeather()
process.generateData()
process.generateFormatted()
process.writeFile()

client = storage.Client.from_service_account_json(jsonKeyfile)
bucket = client.get_bucket('www.fosbergfire.com')
blob = bucket.blob('data.csv')
blob.upload_from_filename('data.csv')

pathToRscript = "C:/Program Files/R/R-3.4.3/bin/Rscript"
pathToFile = "C:/Users/brian/R_Programs/FosbergMapLeaflet.r"
subprocess.call(pathToRscript + " --vanilla " + pathToFile)

blobMap = bucket.blob('map/test.html')
blobMap.upload_from_filename('test.html')

blobMap.make_public()

timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timeStamp)

timeStampFormatted = "Last Updated: " + timeStamp
cssStyle = "html, body {font-family: Lato; font-size: 20px; color: DC5B21; text-align: center; font-weight: 400;}\n"
cssFont = "<link href=\"https://fonts.googleapis.com/css?family=Lato\" rel=\"stylesheet\">\n"

with open('timestamp.html', 'w') as timefile:
    timefile.write(cssFont)
    timefile.write(timeStampFormatted + "\n")
    timefile.write("<style>\n")
    timefile.write(cssStyle)
    timefile.write("</style>")

blobTimeStamp = bucket.blob('misc/timestamp.html')
blobTimeStamp.upload_from_filename('timestamp.html')

blobTimeStamp.make_public()