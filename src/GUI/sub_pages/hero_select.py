from GUI.sub_page import SubPage
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
            position = ((x + (i*space)), y)
            label.place(x=position[0], y=position[1])

            btn = Button(frame, text='SELECT', bg='green', fg='white', font=(txt_font, 8, txt_type),
                         width=btn_w, command=lambda h=hero: self.__on_select(h))
            btn.place(x=position[0], y=position[1]+btn_margin)

            self.add_item_panels(frame, hero.item_images, position[0], position[1]+item_margin)

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

        """
        # Settings
        banner_settings = Label(frame, text=banner_settings_txt, fg=txt_color, bg=default_color, width=txt_width,
                                font=(txt_font, txt_size, txt_type))
        banner_settings.place(x=txt_pos_x, y=txt_pos_y + txt_new_line_y)

        # UI settings labels
        ui_txt_def = Label(frame, text=ui_def_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_def.place(x=ui_txt_pos_x, y=ui_txt_pos_y)

        ui_txt_win = Label(frame, text=ui_win_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_win.place(x=ui_txt_pos_x + ui_new_line_x, y=ui_txt_pos_y)

        ui_txt_vet = Label(frame, text=ui_vet_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_vet.place(x=ui_txt_pos_x + ui_new_line_x * multiplier_2, y=ui_txt_pos_y)

        ui_slider = Scale(frame, from_=min_ui, to=max_ui, length=slider_bar_length, orient=HORIZONTAL, bd=bd_size,
                          sliderlength=slider_length, showvalue=slider_no_value, resolution=ui_slider_res)
        ui_slider.place(x=slider_pos_x, y=slider_pos_y)

        occlusion_label = Label(frame, text=opacity_txt, fg=txt_color, bg=default_color, width=38,
                                font=(txt_font, settings_txt_size, txt_type))
        occlusion_label.place(x=txt_pos_x, y=slider_pos_y + slider_spacing)

        # Change of opacity function with the slider value 'a'
        def alpha(a):
            frame.master.attributes('-alpha', a)

        opacity_slider = Scale(frame, from_=min_opacity, to=max_opacity, length=slider_bar_length, orient=HORIZONTAL,
                               bd=bd_size, sliderlength=slider_length, showvalue=slider_no_value, command=alpha,
                               resolution=opacity_slider_res)
        opacity_slider.place(x=22, y=435)"""

    def __on_select(self, hero):
        options = {'hero': hero}
        self.navigator.show(self.next_page, options)
