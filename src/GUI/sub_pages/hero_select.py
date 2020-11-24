"""
    HeroSelect depends on tkinter, PIL, SubPage, and keys from Hero
"""
from tkinter import Button, Label, Image
from PIL import Image, ImageTk
from GUI.sub_page import SubPage
from GUI.hero import ITEM_IMAGE_KEY

# Keys
HERO_OPTIONS_KEY = 'hero'
HERO_OPT_KEY = 'heroes'

# Text labels
SELECT_MESSAGE = 'SELECT'
TOP_MESSAGE = 'HERO SELECTION'

# Background properties
BACKGROUND_SIZE = (560, 470)
BACKGROUND_COLOR = ("#%02x%02x%02x" % (53, 55, 56))
BACKGROUND_IMAGE_URL = 'assets/images/backgrounds/background_hero.png'

# General properties
TEXT_COLOR = 'white'
TITLE_FONT = ("Arial", 26, 'bold')
BORDER_SIZE = 2

# top label properties
TOP_LABEL_POSITION = (28, 0)
TOP_LABEL_WIDTH = 26

# Hero panel properties
HERO_POSITION = (30, 105)
HERO_SPACE = 178
HERO_ITEM_MARGIN = 220
HERO_ITEM_SPACE = (54, 40)
HERO_ITEMS_EACH_LINE = 3
HERO_BTN_WIDTH = 20
HERO_BTN_MARGIN = 310
HERO_BTN_FONT = ('Arial', 8, 'bold')
HERO_BTN_COLOR = 'green'


class HeroSelect(SubPage):
    """
        HeroSelect is used to create an object that
        can build the required GUI elements which should
        be shown on the hero select page
    """

    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)

    def add_item_panels(self, frame, item_images, x, y):
        """
            Loop through each item image given and
            add them as labels
        """

        i, lines = 0, 0
        for item_image in item_images:

            # increment line number on even indexes
            if i > 0 and i % HERO_ITEMS_EACH_LINE == 0:
                lines += 1

            # Load image
            image = Image.open(item_image[ITEM_IMAGE_KEY])
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, image=image, border=BORDER_SIZE)
            label.image = image
            # Position the label
            _x = (x + (i % HERO_ITEMS_EACH_LINE * HERO_ITEM_SPACE[0]))
            _y = (y + (lines * HERO_ITEM_SPACE[1]))
            label.place(x=_x, y=_y)
            # increase the index to ensure
            # the spacing and lines from
            # the start panel will increase
            i += 1

    def add_hero_panels(self, frame, heroes):
        """
            Loop through each hero and add a label
            containing their avatar, a section with
            their items and a button to select a hero
        """

        i = 0
        # Loop the heroes array
        for hero in heroes:
            # Load image
            image = Image.open(hero.avatar_image_path)
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, image=image)
            label.image = image
            # Position the label
            position = ((HERO_POSITION[0] + (i * HERO_SPACE)), HERO_POSITION[1])
            label.place(x=position[0], y=position[1])
            # Create a button
            btn = Button(frame, text=SELECT_MESSAGE, bg=HERO_BTN_COLOR, fg=TEXT_COLOR, font=HERO_BTN_FONT,
                         width=HERO_BTN_WIDTH, command=lambda h=hero: self.__on_select(h))
            # Position the button
            btn.place(x=position[0], y=position[1] + HERO_BTN_MARGIN)
            # Add the label to the labels array
            self.add_item_panels(frame, hero.item_images, position[0], position[1] + HERO_ITEM_MARGIN)

            # increase the index to ensure
            # the spacing from the start panel
            # will increase
            i += 1

    def build(self, frame, options):
        """
            Clear the given page and builds the sub page
        """
        super().build(frame, options)

        # Load image
        image = Image.open(BACKGROUND_IMAGE_URL)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a label using the image
        label = Label(frame, image=image, width=BACKGROUND_SIZE[0], height=BACKGROUND_SIZE[1])
        label.image = image
        label.grid(row=0, column=0)

        # if any heroes was provided as options
        if options is not None:
            # get the heroes
            heroes = options[HERO_OPT_KEY]
            # add the heroes as panels
            self.add_hero_panels(frame, heroes)

        # create the top label
        top_label = Label(frame, text=TOP_MESSAGE, fg=TEXT_COLOR,
                          bg=BACKGROUND_COLOR, width=TOP_LABEL_WIDTH, font=TITLE_FONT)
        # position the top label
        top_label.place(x=TOP_LABEL_POSITION[1], y=TOP_LABEL_POSITION[0])

    def __on_select(self, hero):
        """
            Navigate to the next page and pass
            the selected hero
        """
        # add the hero passed to the options array
        options = {HERO_OPTIONS_KEY: hero}
        # navigate to the next page using the options
        self.navigator.show(self.next_page, options)
