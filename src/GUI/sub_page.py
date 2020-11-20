class SubPage:

    def __init__(self, navigator, next_page):
        self.navigator = navigator
        self.next_page = next_page

    def build(self, frame, options):
        frame.clear()
