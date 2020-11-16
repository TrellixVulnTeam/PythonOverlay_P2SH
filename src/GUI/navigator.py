from GUI.page import Page
from GUI.sub_pages.hero_select import HeroSelect
from GUI.sub_pages.item_suggestions import ItemSuggestions


# A class used to navigate the sub pages within the main page
class Navigator:
    __main_frame = Page()

    def __init__(self, start_page, heroes):
        self.__heroes = heroes
        self.__sub_pages = [HeroSelect(self, ItemSuggestions), ItemSuggestions(self, HeroSelect)]
        self.__main_frame.pack()
        self.show(start_page)

    def alpha(self, a):
        self.__main_frame.master.attributes('-alpha', a)

    def get_sub_pages(self):
        return self.__sub_pages

    def run(self):
        self.__main_frame.mainloop()

    def show(self, sub_page, options=None):
        if options is None:
            options = {'heroes': self.__heroes}

        for page in self.__sub_pages:
            if type(page) is sub_page:
                page.build(self.__main_frame, options)
