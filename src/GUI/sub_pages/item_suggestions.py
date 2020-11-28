"""
    ItemSuggestions depends on tkinter, PIL, SubPage and static Hero keys
"""
from tkinter import Button, Label, LEFT, Toplevel, CENTER
from PIL import Image, ImageTk
import pyautogui
from GUI.sub_page import SubPage
from GUI.hero import ITEM_IMAGE_KEY, ITEM_DESC_KEY, ITEM_DESC_NAME
from GUI.sub_pages.hero_select import HERO_OPTIONS_KEY

# Background properties
BACKGROUND_IMAGE_URL = "assets/images/backgrounds/background_hero.png"
BACKGROUND_SIZE = (180, 160)
BACKGROUND_COLOR = ("#%02x%02x%02x" % (53, 55, 56))

# General properties
TEXT_COLOR = 'white'
TITLE_FONT = ("Arial", 16)
PARAGRAPH_FONT = ("Arial", 8)
BORDER_SIZE = 2
COMPOUND = 'center'
ANCHOR = 'w'
GEOMETRY_PATTERN = "%dx%d+%d+%d"
TOP_OPT_KEY = '-topmost'

# Text labels
BACK_MESSAGE = 'BACK'
NO_ITEM = 'ERROR: NO ITEM'

# Hero panel properties
BTN_COLOR = 'black'
BTN_POSITION = (10, 10)
BTN_SIZE = (40, 160)

# Item panel properties
ITEM_POSITION = (10, 65)
ITEM_SPACE = (60, 45)
ITEM_EACH_LINE = 3
ITEM_DESC_MARGIN = 50
ITEM_WIDTH = 20

# Tooltip properties
TOOLTIP_NAME_COLOR = 'yellow'
TOOLTIP_WIDTH = 300
TOOLTIP_HEIGHT = 60
TOOLTIP_X_OFFSET = 200
TOOLTIP_Y_OFFSET = -30
TOOLTIP_DESC_Y = 18


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
        self.item_descriptions = []
        self.item_names = []

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
                     height=BTN_SIZE[0], width=BTN_SIZE[1], bg=BTN_COLOR, border=BORDER_SIZE, command=self.on_click)
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
        self.item_descriptions = []
        self.item_names = []

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

            # bind mouse events
            label.bind("<Enter>", self.__on_enter)
            label.bind("<Leave>", self.__on_leave)

            # Save name and description for later
            self.item_names.append(item_image[ITEM_DESC_NAME])
            self.item_descriptions.append(item_image[ITEM_DESC_KEY])

            # save label for later
            self.item_labels.append(label)
            # increase the index to ensure
            # the spacing and lines from
            # the start panel will increase
            i += 1

    def add_item_background(self, frame, width=BACKGROUND_SIZE[0], height=BACKGROUND_SIZE[1]):
        """
            Adds a label that functions as a background
            for the item suggestions page
        """

        # Load image
        image = Image.open(BACKGROUND_IMAGE_URL)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a label using the image
        label = Label(frame, image=image, width=width, height=height)
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

        # cache page
        self.page = page

    def on_click(self):
        """
            Disables the sub page and navigate to the next page
        """
        self.is_active = False
        self.navigator.show(self.next_page)

    def __on_enter(self, event):
        """
            Find a name and description matching the item the mouse is currently
            hovering, and adds a tooltip above the window with the information
        """

        # get name and description
        name, desc = self.__get_item_desc_at_mouse_pos()
        # get window position
        y, x = self.page.winfo_rooty(), self.page.winfo_rootx()
        # create tooltip as toplevel window
        self.top = Toplevel(self.page)
        # set tooltip position, size, and offset
        self.top.geometry(GEOMETRY_PATTERN % (TOOLTIP_WIDTH, TOOLTIP_HEIGHT,
                                              x + TOOLTIP_X_OFFSET, y + TOOLTIP_Y_OFFSET))
        # ensure the toplevel window is borderless
        self.top.overrideredirect(1)
        # ensure the top level window stay on top
        self.top.wm_attributes(TOP_OPT_KEY, 2)
        # add a background to the top level window
        self.add_item_background(self.top, TOOLTIP_WIDTH, TOOLTIP_HEIGHT)

        # add item name
        label = Label(self.top, text=name, fg=TOOLTIP_NAME_COLOR, justify=LEFT, anchor=ANCHOR,
                      compound=COMPOUND, bg=BACKGROUND_COLOR, width=TOOLTIP_WIDTH, font=PARAGRAPH_FONT)
        # position item name
        label.place(x=0, y=0)

        # add item description
        label = Label(self.top, text=desc, fg=TEXT_COLOR, justify=LEFT, anchor=ANCHOR,
                      compound=COMPOUND, bg=BACKGROUND_COLOR, width=TOOLTIP_WIDTH, font=PARAGRAPH_FONT)
        # position item description
        label.place(x=0, y=TOOLTIP_DESC_Y)

    def __on_leave(self, event):
        """
            Destroy the latest tooltip window
        """

        # if th tooltip exist
        if self.top is not None:
            # destroy it
            self.top.destroy()

    def __get_item_desc_at_mouse_pos(self):
        """
            Returns an item description matching the item
            the mouse is currently hovering
        """
        # get mouse position
        x, y = pyautogui.position()
        # returns a no item message in case of error
        name, desc = NO_ITEM, NO_ITEM
        # loop all labels
        for i in range(0, len(self.item_labels)):
            # get current label
            l = self.item_labels[i]
            # get label position
            ly, lx = l.winfo_rooty(), l.winfo_rootx()
            # get label size
            lw, lh = l.winfo_reqwidth(), l.winfo_reqheight()
            # check if the mouse x and y is within the label
            # position and size
            if ly <= y <= ly + lh and \
                    lx <= x <= lx + lw:
                # find a corresponding item description
                name = self.item_names[i]
                desc = self.item_descriptions[i]
                # stop the loop
                break
        # return the item description
        return name, desc
