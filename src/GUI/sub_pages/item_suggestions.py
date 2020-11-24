"""
    ItemSuggestions depends on tkinter, PIL, SubPage and static Hero keys
"""
from tkinter import Button, Label, LEFT
from PIL import Image, ImageTk
from GUI.sub_page import SubPage
from GUI.hero import ITEM_IMAGE_KEY, ITEM_DESC_KEY
from GUI.sub_pages.hero_select import HERO_OPTIONS_KEY


# Background properties
BACKGROUND_IMAGE_URL = "assets/images/backgrounds/background_hero.png"
BACKGROUND_SIZE = (180, 400)
BACKGROUND_COLOR = ("#%02x%02x%02x" % (53, 55, 56))

# General properties
TEXT_COLOR = 'white'
TITLE_FONT = ("Arial", 16)
PARAGRAPH_FONT = ("Arial", 8)
BORDER_SIZE = 2
COMPOUND = 'center'
ANCHOR = 'w'

# Text labels
BACK_MESSAGE = 'BACK'

# Hero panel properties
BTN_COLOR = 'black'
BTN_POSITION = (10, 10)
BTN_SIZE = (40, 160)

# Item panel properties
ITEM_POSITION = (10, 75)
ITEM_SPACE = (80, 55)
ITEM_EACH_LINE = 1
ITEM_DESC_MARGIN = 50
ITEM_WIDTH = 20


class ItemSuggestions(SubPage):
    """
        ItemSuggestions is used to create an object that
        can build the required GUI elements which should
        be shown on the item suggestion page
    """

    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)
        # a reference to each item label
        # used to indicate an item was found
        self.item_labels = []

        # the last selected hero
        # used to get item suggestions
        # mapped to the hero
        self.last_hero = None

        # used to indicate whether or not
        # this sub page is active
        self.is_active = False

    def add_hero_panel(self, frame, hero):
        """
            Creates a button that display an image of the hero
            that can be used to navigate back to the hero select page
        """

        # Load image
        image = Image.open(hero.avatar_image_path)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a button using the image
        btn = Button(frame, image=image, text=BACK_MESSAGE, fg=TEXT_COLOR, compound=COMPOUND, font=TITLE_FONT,
                     height=BTN_SIZE[0], width=BTN_SIZE[1], bg=BTN_COLOR, border=BORDER_SIZE, command=self.__on_click)
        btn.image = image
        # Position the button
        btn.place(x=BTN_POSITION[0], y=BTN_POSITION[1])

    def add_item_panels(self, frame, hero):
        """
            Loops through the hero's item suggestions
            and add a label for each item with a description
        """

        # reset item label array
        self.item_labels = []

        i, lines = 0, 0
        for item_image in hero.item_images:

            # increment line number on even indexes
            if i > 0 and i % ITEM_EACH_LINE == 0:
                lines += 1

            # Load image
            image = Image.open(item_image[ITEM_IMAGE_KEY])
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, text=f'{i}', image=image, border=BORDER_SIZE,
                          compound=COMPOUND, fg=TEXT_COLOR, font=TITLE_FONT)
            label.image = image
            # Position the label
            x = (ITEM_POSITION[0] + (i % ITEM_EACH_LINE * ITEM_SPACE[0]))
            y = (ITEM_POSITION[1] + (lines * ITEM_SPACE[1]))
            label.place(x=x, y=y)
            # Create a label for the item description
            desc = Label(frame, text=item_image[ITEM_DESC_KEY], fg=TEXT_COLOR, justify=LEFT, anchor=ANCHOR,
                         compound=COMPOUND, bg=BACKGROUND_COLOR, width=ITEM_WIDTH, font=PARAGRAPH_FONT)
            # Position the label
            desc.place(x=x+ITEM_DESC_MARGIN, y=y)

            # save label for later
            self.item_labels.append(label)
            # increase the index to ensure
            # the spacing and lines from
            # the start panel will increase
            i += 1

    def add_item_background(self, frame):
        """
            Adds a label that functions as a background
            for the item suggestions page
        """

        # Load image
        image = Image.open(BACKGROUND_IMAGE_URL)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a label using the image
        label = Label(frame, image=image, width=BACKGROUND_SIZE[0], height=BACKGROUND_SIZE[1])
        label.image = image
        label.grid(row=0, column=0)

    def build(self, page, options):
        """
            Clear the given page and builds the sub page
        """
        super().build(page, options)
        self.add_item_background(page)

        if options is not None:
            self.last_hero = options[HERO_OPTIONS_KEY]
            self.add_hero_panel(page, self.last_hero)
            self.add_item_panels(page, self.last_hero)
            self.is_active = True

    def __on_click(self):
        """
            Disables the sub page and navigate to the next page
        """
        self.is_active = False
        self.navigator.show(self.next_page)
