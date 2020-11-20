from ground_truth.reader import Reader
import csv


class GroundTruth:
    __true_positive = 0
    __false_positive = 0
    __false_negative = 0
    __true_negative = 0

    def __init__(self, file_path):
        r = Reader(file_path)
        self.__data = r.get_data()

    def get_data(self):
        return self.__data

    def increase_by(self, item_truth, detection_truth):
        # TP
        if item_truth and detection_truth:
            self.__true_positive += 1
        # TN
        elif not item_truth and not detection_truth:
            self.__true_negative += 1
        # FN
        elif item_truth and not detection_truth:
            self.__false_negative += 1
        # FP
        elif not item_truth and detection_truth:
            self.__false_positive += 1

    def get_accuracy(self):
        t = (self.__true_negative + self.__true_positive)
        total = (self.__true_negative + self.__false_positive +
                 self.__false_negative + self.__true_positive)
        return t / total

    def get_precision(self):
        total = (self.__true_positive + self.__false_positive)
        return self.__true_positive / total

    def get_recall(self):
        total = (self.__true_positive + self.__false_negative)
        return self.__true_positive / total

    def save(self, file_path):
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['TP', 'FP', 'FN', 'TN', 'Accuracy', 'Precision', 'Recall']
            res = {
                'TP': self.__true_positive,
                'FP': self.__false_positive,
                'FN': self.__false_negative,
                'TN': self.__true_negative,
                'Accuracy': self.get_accuracy(),
                'Precision': self.get_precision(),
                'Recall': self.get_recall()
            }
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(res)
