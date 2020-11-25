"""
    The navigator depends on the Page, HeroSelect, and ItemSuggestions classes
"""
from GUI.page import Page
from GUI.sub_pages.hero_select import HeroSelect
from GUI.sub_pages.item_suggestions import ItemSuggestions


# A key used to specify heroes within
# the option args. passed to a sub page
HERO_OPT_KEY = 'heroes'

# Keys used to change behavior and presentation
# of the window attached to the main frame
TOP_OPT_KEY = '-topmost'
ALPHA_OPT_KEY = '-alpha'


class Navigator:
    """
        A class used to instantiate and navigate the sub pages within the main page
    """

    # A reference to the navigator's only frame
    __main_frame = Page()

    def __init__(self, heroes, start_page=HeroSelect):
        # Save references for later.
        self.__heroes = heroes
        self.__sub_pages = [HeroSelect(self, ItemSuggestions),
                            ItemSuggestions(self, HeroSelect)]
        # Ensure the frame stays on top of other windows
        self.__main_frame.master.wm_attributes(TOP_OPT_KEY, 1)
        # Pack widgets using horizontal and vertical boxes
        self.__main_frame.pack()
        # Show the first sub page
        self.show(start_page)

    def get_item_suggestions_page(self):
        """
            return the item suggestions sub page
        """
        return self.__sub_pages[1]

    def get_main_frame(self):
        """
            Returns the main frame
        """
        return self.__main_frame

    def alpha(self, value):
        """
            Change the opacity of the navigator's frame
        """
        self.__main_frame.master.attributes(ALPHA_OPT_KEY, value)

    def get_sub_pages(self):
        """
            Returns an array with sub pages
        """
        return self.__sub_pages

    def run(self):
        """
            Show the frame's current widgets
        """
        self.__main_frame.mainloop()

    def show(self, sub_page, options=None):
        """
            Change the current sub page that is
            currently being displayed.
        """

        # If no options were given, we just pass
        # the heroes as option to be able show the
        # hero select page without passing them as
        # options everytime.
        if options is None:
            options = {HERO_OPT_KEY: self.__heroes}

        # Then, we loop all sub pages to find the
        # sub page with the same instance type as
        # the one passed as an argument (page)
        for page in self.__sub_pages:
            if isinstance(page, sub_page):
                page.build(self.__main_frame, options)
                break
