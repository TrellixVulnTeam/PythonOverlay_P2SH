"""
    The ground truth reader depends on the DictReader class from csv,
    and 'sub' method from re
"""
from csv import DictReader
from re import sub


# reference options
TIME_KEY = 'time'
ITEMS_KEY = 'items'

# parse options
TIME_P_KEY = 'Tid'
ITEM_P_KEY = 'item'
TIME_P_REG = '\s+|sec|\''
ITEM_P_REG = '\[|]'
P_DELIMITER = ";"
N_ITEMS = 6


class GTReader:
    """
        The ground truth is used to create an object that can read
        a csv file representing ground truth data
    """

    # Used to reference the formatted data
    # read from the specified csv file
    __data = []

    def __init__(self, file_path):
        # Read the csv file when instantiated
        self.__read_csv(file_path)

    def __read_csv(self, file_path):
        """
            Reads a csv file at the given file path
            and format the data in an array of objs.
            formatted as {"time": int, "items": list}
        """

        # Ensure the data array is empty
        self.__data = []

        # Open the csv file
        with open(file_path, newline='') as csv_file:

            # read the csv file using a specified delimiter (comma, semi-colon, etc.)
            reader = DictReader(csv_file, delimiter=P_DELIMITER)
            # loop through each row within the csv file
            for row in reader:

                # remove white spaces and letters from time string
                seconds = sub(TIME_P_REG, '', row[TIME_P_KEY])
                # format datum object using the time as float and an empty list
                datum = {TIME_KEY: float(seconds), ITEMS_KEY: []}

                # loop from zero to the number of items expected within the csv file
                for i in range(0, N_ITEMS):

                    # remove '[]' from the item string arrays
                    item_str_array = sub(ITEM_P_REG, "", row[f'{ITEM_P_KEY}{i + 1}'])
                    # split the item string array based on comma and return a list
                    # of the integers found within the item string array
                    item_location = [int(s) for s in item_str_array.split(',') if s.isdigit()]
                    # append the formatted int array to the datum's item list
                    datum[ITEMS_KEY].append(item_location)

                # append the datum object to the data list
                self.__data.append(datum)

    def get_data(self):
        """
           Returns the array of formatted data
        """
        return self.__data
