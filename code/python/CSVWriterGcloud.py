import csv
import os

import cloudstorage as gcs
from google.appengine.api import app_identity



class CSVWriter(object):
    def __init__(self):
        self.bucket_name = os.environ.get(
        'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
        self.write_retry_params = gcs.RetryParams(backoff_factor=1.1)
        self.filename = os.path.join(self.bucket_name, 'data.csv')
        self.header = ['County', 'Index', 'Temperature', 'Humidity', 'Wind', 'Websites']

    def writeLines(self, formatted):
        gcs_file = gcs.open(self.filename, 'w', content_type='text/csv', retry_params=self.write_retry_params)
        csvwriter = csv.writer(gcs_file, delimiter='\t')
        csvwriter.writerow(self.header)
        csvwriter.writerows(formatted)