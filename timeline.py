import csv
import urllib2
import secret

class Timeline():
    def __init__(self):
        self.category_dict = {}

    def get_data_from_local_csv(self):
        with open("data.csv", 'r') as csv_file:
            csv_content = csv.reader(csv_file)
            for row in csv_content:
                for col in row:
                    print col
