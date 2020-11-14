from GUI.page import Page
from GUI.sub_pages.hero_select import HeroSelect
from GUI.sub_pages.item_suggestions import ItemSuggestions


# A class used to navigate the sub pages within the main page
class Navigator:
    __main_frame = Page()

    def __init__(self, start_page):
        self.__sub_pages = [HeroSelect(self, ItemSuggestions), ItemSuggestions(self, HeroSelect)]
        self.__main_frame.pack()
        self.__main_frame.master.title("My Do-Nothing Application")
        self.show(start_page)

    def alpha(self, a):
        self.__main_frame.master.attributes('-alpha', a)

    def run(self):
        self.__main_frame.mainloop()

    def show(self, sub_page):
        for page in self.__sub_pages:
            if type(page) is sub_page:
                page.build(self.__main_frame)
