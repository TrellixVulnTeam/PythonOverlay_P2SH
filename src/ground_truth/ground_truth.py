import csv


class GroundTruth:
    true_positive = 0
    false_positive = 0
    false_negative = 0
    true_negative = 0

    def increase_by(self, item_truth, detection_truth):
        # TP
        if item_truth and detection_truth:
            self.true_positive += 1
        # TN
        elif not item_truth and not detection_truth:
            self.true_negative += 1
        # FN
        elif item_truth and not detection_truth:
            self.false_negative += 1
        # FP
        elif not item_truth and detection_truth:
            self.false_positive += 1

    def save(self, file_path):
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['TP', 'FP', 'FN', 'TN']
            res = {
                'TP': self.true_positive,
                'FP': self.false_positive,
                'FN': self.false_negative,
                'TN': self.true_negative
            }
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(res)
