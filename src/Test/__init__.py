from tkinter import Frame
from tkinter import Button, Label, HORIZONTAL, Scale, Canvas, Image
from PIL import Image, ImageTk

# Window properties
hero_size = "520x540"
bg_image_hero = "assets/images/backgrounds/background_hero.png"

multiplier_2 = 2
multiplier_3 = 3

# Hero image properties
hero_tank = "assets/images/heroes/underlord.png"
hero_agility = "assets/images/heroes/anti_mage.png"
hero_mage = "assets/images/heroes/shadow_shaman.png"
origin = 0
hero_img_pos_x = -132.5
hero_img_pos_y = 40
bd_size = 0
selected_hero = hero_tank

# Slider properties
slider_pos_x = 22
slider_pos_y = 371
slider_spacing = 33
min_opacity = 0.1
max_opacity = 1
min_ui = 1
max_ui = 3
slider_length = 150
slider_bar_length = 463
ui_slider_res = 1
opacity_slider_res = 0.01
slider_no_value = 0

# Localization
banner_hero_txt = "HERO SELECTION"
banner_settings_txt = "Settings"

ui_def_txt = "Default"
ui_win_txt = "Windowed"
ui_vet_txt = "Veteran"
opacity_txt = "Opacity"

# Text properties
settings_txt_size = 14
ui_txt_pos_x = 25
ui_txt_pos_y = 340
ui_txt_width = 12

ui_new_line_x = 156
txt_new_line_y = 270
new_line_y = 20
new_line_x = 157.5

txt_pos_x = 25
txt_pos_y = 10
txt_size = 26
txt_width = 24
txt_font = "arial"
txt_type = 'bold'
txt_color = 'white'
default_color = 'gray'
highlight_color = 'green'


class Page(Frame):

    def __init__(self, **kw):
        super().__init__(**kw)

    def clear(self):
        for w in self.winfo_children():
            w.destroy()


class SubPage:

    def __init__(self, navigator, next_page):
        self.navigator = navigator
        self.next_page = next_page

    def build(self, frame, options):
        frame.clear()


class Hero:

    def __init__(self, avatar_image, item_images, item_images_ref):
        self.avatar_image = avatar_image
        self.item_images = item_images
        self.item_images_ref = item_images_ref


class ItemSuggestions(SubPage):
    item_background_image_url = "assets/images/backgrounds/background_hero.png"
    item_highlight_color = 'green'
    item_position = (10, 75)
    item_space = (80, 55)
    item_each_line = 1

    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)
        self.last_hero = None
        self.is_active = False
        self.item_labels = []

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
            label = Label(frame, text=f'{i}', image=image, border=2, compound='center', fg='red',
                          font=("Arial", 16))  # , bg=self.item_highlight_color
            label.image = image
            # Position the label
            _x = (x + (i % self.item_each_line * self.item_space[0]))
            _y = (y + (lines * self.item_space[1]))
            label.place(x=_x, y=_y)

            desc = Label(frame, text=item_image['desc'], fg='white', justify=LEFT, anchor="w", compound='center', bg=bg,
                         width=w, font=("Arial", 8))
            desc.place(x=_x + desc_margin, y=_y)

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


class HeroSelect(SubPage):
    item_space = (54, 40)
    item_each_line = 3

    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)

    def add_item_panels(self, frame, item_images, x, y):
        r = 30
        # First panel position
        i, lines = 0, 0
        for item_image in item_images:

            # increment line number on even indexes
            if i > 0 and i % self.item_each_line == 0:
                lines += 1

            # Load image
            image = Image.open(item_image['image'])
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, image=image, border=2)
            label.image = image
            # Position the label
            _x = (x + (i % self.item_each_line * self.item_space[0]))
            _y = (y + (lines * self.item_space[1]))
            label.place(x=_x, y=_y)
            # increase the index to ensure
            # the spacing and lines from
            # the start panel will increase
            i += 1

    def add_hero_panels(self, frame, heroes):
        # First panel position
        x, y, item_margin = 30, 105, 220
        btn_margin, btn_w = 310, 20
        # Panel spacing and index
        space, i = 178, 0
        # Loop the heroes array
        for hero in heroes:
            # Load image
            image = Image.open(hero.avatar_image)
            # get image as ImageTK
            image = ImageTk.PhotoImage(image)
            # Create a label using the image
            label = Label(frame, image=image)
            label.image = image
            # Position the label
            position = ((x + (i * space)), y)
            label.place(x=position[0], y=position[1])

            btn = Button(frame, text='SELECT', bg='green', fg='white', font=(txt_font, 8, txt_type),
                         width=btn_w, command=lambda h=hero: self.__on_select(h))
            btn.place(x=position[0], y=position[1] + btn_margin)

            self.add_item_panels(frame, hero.item_images, position[0], position[1] + item_margin)

            # increase the index to ensure
            # the spacing from the start panel
            # will increase
            i += 1

    def build(self, frame, options):
        super().build(frame, options)

        # Load image
        image = Image.open(bg_image_hero)
        # get image as ImageTK
        image = ImageTk.PhotoImage(image)
        # Create a label using the image
        label = Label(frame, image=image, width=560, height=470)
        label.image = image
        label.grid(row=0, column=0)

        if options is not None:
            heroes = options['heroes']
            self.add_hero_panels(frame, heroes)

        x, y, w = 0, 28, 26
        font = (txt_font, txt_size, txt_type)
        # Hero roster
        bg = ("#%02x%02x%02x" % (53, 55, 56))
        banner_hero = Label(frame, text=banner_hero_txt, fg=txt_color, bg=bg, width=w, font=font)
        banner_hero.place(x=x, y=y)

    def __on_select(self, hero):
        options = {'hero': hero}
        self.navigator.show(self.next_page, options)


# A class used to navigate the sub pages within the main page
class Navigator:
    __main_frame = Page()

    def __init__(self, start_page, heroes):
        self.__heroes = heroes
        self.__sub_pages = [HeroSelect(self, ItemSuggestions), ItemSuggestions(self, HeroSelect)]

        self.__main_frame.master.wm_attributes("-topmost", 1)  # keep on top
        # self.__main_frame.master.overrideredirect(1)  # remove border
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
