import csv
import re
from dateutil import parser

"""
r = Reader('assets/csv/sample_data.csv')
print(r.data)
"""


class Reader:
    # reference options
    __TIME_KEY = 'time'
    __ITEMS_KEY = 'items'

    # parse options
    __TIME_P_KEY = 'Tid'
    __ITEM_P_KEY = 'item'
    __TIME_P_REG = '\s+|sec|\''
    __ITEM_P_REG = '\[|]'
    __N_ITEMS = 6

    # parsed data
    __data = []

    def __init__(self, file_path):
        self.read_csv(file_path)

    def read_csv(self, file_path):
        # reset data on read
        self.__data = []

        with open(file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:

                seconds = re.sub(self.__TIME_P_REG, '', row[self.__TIME_P_KEY])
                time = float(seconds)  # parser.parse(row[self.__TIME_P_KEY])

                datum = {self.__TIME_KEY: time, self.__ITEMS_KEY: []}

                for i in range(0, self.__N_ITEMS):
                    item_str_array = re.sub(self.__ITEM_P_REG, "", row[f'{self.__ITEM_P_KEY}{i + 1}'])
                    item_location = [int(s) for s in item_str_array.split(',') if s.isdigit()]
                    datum[self.__ITEMS_KEY].append(item_location)

                self.__data.append(datum)

    def get_data(self):
        return self.__data
