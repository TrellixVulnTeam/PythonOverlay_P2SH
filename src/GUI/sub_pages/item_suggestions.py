from GUI.sub_page import SubPage
from tkinter import Button, Label, LEFT
from PIL import Image, ImageTk


class ItemSuggestions(SubPage):

    item_background_image_url = "assets/images/backgrounds/background_hero.png"
    item_highlight_color = 'green'
    item_position = (10, 75)
    item_space = (80, 55)
    item_each_line = 1
    item_labels = []

    last_hero = None
    is_active = False

    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)

    def add_hero_panel(self, frame, hero):
        # Load image
        image = Image.open(hero.avatar_image)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a button using the image
        btn = Button(frame, image=image, text='BACK', fg='white', compound='center', font=("Arial", 16),
                     height=40, width=160, bg='black', border=2, command=self.__on_click)
        btn.image = image
        # Position the button
        btn.place(x=10, y=10)

    def add_item_panels(self, frame, hero):
        # reset item label array
        self.item_labels = []
        # First panel position
        x, y = self.item_position[0], self.item_position[1]
        i, lines = 0, 0
        desc_margin, w = 50, 20
        bg = ("#%02x%02x%02x" % (53, 55, 56))
        font = ("Arial", 16)
        for item_image in hero.item_images:

            # increment line number on even indexes
            if i > 0 and i % self.item_each_line == 0:
                lines += 1

            # Load image
            image = Image.open(item_image['image'])
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, text=f'{i}', image=image, border=2, compound='center', fg='red', font=("Arial", 16))  # , bg=self.item_highlight_color
            label.image = image
            # Position the label
            _x = (x + (i % self.item_each_line * self.item_space[0]))
            _y = (y + (lines * self.item_space[1]))
            label.place(x=_x, y=_y)

            desc = Label(frame, text=item_image['desc'], fg='white', justify=LEFT, anchor="w", compound='center', bg=bg, width=w, font=("Arial", 8))
            desc.place(x=_x+desc_margin, y=_y)

            # save label for later
            self.item_labels.append(label)
            # increase the index to ensure
            # the spacing and lines from
            # the start panel will increase
            i += 1

    def add_item_background(self, frame):
        # Load image
        image = Image.open(self.item_background_image_url)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a label using the image
        label = Label(frame, image=image, width=180, height=400)
        label.image = image
        label.grid(row=0, column=0)

    def build(self, frame, options):
        super().build(frame, options)

        self.add_item_background(frame)

        if options is not None:
            self.last_hero = options['hero']
            self.add_hero_panel(frame, self.last_hero)
            self.add_item_panels(frame, self.last_hero)
            self.is_active = True

    def __on_click(self):
        self.is_active = False
        self.navigator.show(self.next_page)
