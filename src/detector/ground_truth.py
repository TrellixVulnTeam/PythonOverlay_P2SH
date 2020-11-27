"""
    The ground truth depends on the GTReader, and DictWriter classes
"""
from csv import DictWriter
from detector.gt_reader import GTReader


# The field names represented within the result csv file
FIELD_NAMES = ['TP', 'FP', 'FN', 'TN', 'Accuracy', 'Precision', 'Recall']

# The location of the csv where the object should write the result to
FILE_PATH = 'assets/csv/result.csv'


class GroundTruth:
    """
        GroundTruth is used to create an object that count TP, FP, FN, TN
        situations, which is use to calculate an accuracy, precision and recall
        and save it to a csv file with the results
    """

    # True positive, False positive
    # False negative, True negative
    __tp, __fp, __fn, __tn = 0, 0, 0, 0

    def __init__(self, file_path):
        # Read a ground truth csv file at the given file path
        reader = GTReader(file_path)
        # Save the data read from the specified csv file
        self.__data = reader.get_data()

    def __get_accuracy(self):
        """
            Returns the accuracy based on the current values of TP, FP, FN, TN
        """
        return (self.__tn + self.__tp) / (self.__tn + self.__fp + self.__fn + self.__tp)

    def __get_precision(self):
        """
            Returns the precision based on the current values of TP, FP, FN, TN
        """
        return self.__tp / (self.__tp + self.__fp)

    def __get_recall(self):
        """
            Returns the recall based on the current values of TP, FP, FN, TN
        """
        return self.__tp / (self.__tp + self.__fn)

    def get_data(self):
        """
            Returns an array with ground truth data where each iteration
            represents a frame, where time and the current existence of
            reference items is specified
        """
        return self.__data

    def increase_by(self, item_truth, detection_truth, within_roi_truth):
        """
            Increase TP, FP, FN, or TN based on the truthfulness of the
            detection compared to the truthfulness of the matched ground truth data
        """

        # Note: tp can only increase if there actual was an item,
        # it was detected, and the detection was at the correct location.
        if item_truth and detection_truth and within_roi_truth:
            self.__tp += 1
        elif not item_truth and not detection_truth:
            self.__tn += 1
        elif item_truth and not detection_truth:
            self.__fn += 1
        elif not item_truth and detection_truth:
            self.__fp += 1

    def save(self):
        """
             Write results based on the current TP, FP, FN, TN values to a csv file
             located at the given file path
        """

        # Open the csv file at the given file path
        with open(FILE_PATH, 'w', newline='') as csv_file:

            # format and calculate results
            res = {
                FIELD_NAMES[0]: self.__tp,
                FIELD_NAMES[1]: self.__fp,
                FIELD_NAMES[2]: self.__fn,
                FIELD_NAMES[3]: self.__tn,
                FIELD_NAMES[4]: self.__get_accuracy(),
                FIELD_NAMES[5]: self.__get_precision(),
                FIELD_NAMES[6]: self.__get_recall()
            }

            # Write results to the csv file
            writer = DictWriter(csv_file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerow(res)

    def reset(self):
        """
            Reset the current values of TP, FP, FN, TN
        """
        self.__tp = 0
        self.__fp = 0
        self.__fn = 0
        self.__tn = 0
