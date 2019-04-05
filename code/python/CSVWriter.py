import csv

class CSVWriter(object):
    def __init__(self):
        self.csvPath = 'data.csv'
        self.header = ['County', 'Index', 'Temperature', 'Humidity', 'Wind', 'Websites']

    def writeLines(self, formatted):
        with open(self.csvPath, 'w', newline= '') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.header)
            csvwriter.writerows(formatted)
