

class SubPage:
    """
        SubPage is used to define pages within the Page type.
        This is done by subclassing this class and override the build
        method, and call the super method to clear the passed page's widgets.
        After this is done can the sub pages widget be added within the build method.
    """

    def __init__(self, navigator, next_page):
        # The navigator creating this sub page is referenced
        # in order to use the navigator's switch method later
        self.navigator = navigator
        # next page defines the sub page type that should be
        # drawn if a navigation switch is executed from a sub page
        self.next_page = next_page

    def build(self, page, options):
        """
            Used to destroy current page widgets before adding new
        """
        page.clear()
