

class ROI:

    y_start = 0
    x_start = 0
    y_end = 0
    x_end = 0

    # The class constructor.
    # Requires a x and y range
    def __init__(self, y_start, y_end, x_start, x_end):
        self.y_start = y_start
        self.x_start = x_start
        self.y_end = y_end
        self.x_end = x_end

    def __init__(self, y_ranges, x_ranges):
        self.y_ranges = y_ranges
        self.x_ranges = x_ranges