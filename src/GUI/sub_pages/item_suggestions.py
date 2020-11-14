from GUI.sub_page import SubPage
from tkinter import Button, Label
from PIL import Image, ImageTk

# Window properties
build_size = "320x198"
bg_image_build = "assets/image/backgrounds/background_build.png"

multiplier_2 = 2
multiplier_3 = 3

# Hero image properties
hero_tank = "assets/image/heroes/underlord.png"
hero_agility = "assets/image/heroes/anti_mage.png"
hero_mage = "assets/image/heroes/shadow_shaman.png"
origin = 0
hero_img_pos_x = -132.5
hero_img_pos_y = 40
bd_size = 0
selected_hero = hero_tank

# Item image properties
img_1 = "assets/image/items/quelling_blade.png"
img_2 = "assets/image/items/belt_of_strength.png"
img_3 = "assets/image/items/crown.png"
img_4 = "assets/image/items/boots_of_speed.png"
img_5 = "assets/image/items/chainmail.png"
img_6 = "assets/image/items/ogre_axe.png"
img_pos_x = 80
img_pos_y = -55
new_img_line_y = 65
new_img_line_x = 80

highlight_color = 'green'


class ItemSuggestions(SubPage):
    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)

    def build(self, frame):
        super().build(frame)

        #green_button = Button(frame, text="Brown", fg="brown", command=self.__on_click)
        #green_button.pack(side=RIGHT)

        # ... hero select widgets
        load = Image.open(bg_image_build)
        render = ImageTk.PhotoImage(load)
        img_bg = Label(frame, image=render, bd=bd_size)
        img_bg.image = render
        img_bg.grid(row=origin, column=origin)

        # Hero image and return button
        load = Image.open(selected_hero)
        render = ImageTk.PhotoImage(load)
        img_hero = Button(frame, image=render, bd=bd_size, command=self.__on_click)
        img_hero.image = render
        img_hero.place(x=origin, y=origin)

        # Abilities for build
        load = Image.open(img_1)
        render = ImageTk.PhotoImage(load)
        item_1 = Label(frame, image=render, bg=highlight_color)
        item_1.image = render
        item_1.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y)

        load = Image.open(img_2)
        render = ImageTk.PhotoImage(load)
        item_2 = Label(frame, image=render, bg=highlight_color)
        item_2.image = render
        item_2.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_2)

        load = Image.open(img_3)
        render = ImageTk.PhotoImage(load)
        item_3 = Label(frame, image=render, bg=highlight_color)
        item_3.image = render
        item_3.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_3)

        load = Image.open(img_4)
        render = ImageTk.PhotoImage(load)
        item_4 = Label(frame, image=render, bg=highlight_color)
        item_4.image = render
        item_4.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y)

        load = Image.open(img_5)
        render = ImageTk.PhotoImage(load)
        item_5 = Label(frame, image=render, bg=highlight_color)
        item_5.image = render
        item_5.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_2)

        load = Image.open(img_6)
        render = ImageTk.PhotoImage(load)
        item_6 = Label(frame, image=render, bg=highlight_color)
        item_6.image = render
        item_6.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_3)

    def __on_click(self):
        self.navigator.show(self.next_page)
