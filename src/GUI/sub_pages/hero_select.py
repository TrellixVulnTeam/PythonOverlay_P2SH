from GUI.sub_page import SubPage
from tkinter import Button, Label, HORIZONTAL, Scale
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
banner_hero_txt = "Select a Hero"
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
txt_size = 24
txt_width = 24
txt_font = "arial"
txt_type = 'bold'
txt_color = 'white'
default_color = 'gray'
highlight_color = 'green'


class HeroSelect(SubPage):
    def __init__(self, navigator, next_page):
        super().__init__(navigator, next_page)

    def build(self, frame):
        super().build(frame)

    # red_button = Button(frame, text="Red", fg="red", command=self.__on_select)
       # red_button.pack(side=LEFT)

        # ... hero select widgets
        load = Image.open(bg_image_hero)
        render = ImageTk.PhotoImage(load)
        img = Label(frame, image=render, bd=bd_size)
        img.image = render
        img.grid(row=origin, column=origin)

        # Hero roster
        banner_hero = Label(frame, text=banner_hero_txt, fg=txt_color, bg=default_color, width=txt_width,
                            font=(txt_font, txt_size, txt_type))
        banner_hero.place(x=txt_pos_x, y=txt_pos_y)

        load = Image.open(hero_tank)
        render = ImageTk.PhotoImage(load)
        img = Button(frame, image=render, bd=bd_size, command=self.__on_select)
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x, y=hero_img_pos_y + new_line_y)

        load = Image.open(hero_agility)
        render = ImageTk.PhotoImage(load)
        img = Button(frame, image=render, bd=bd_size, command=self.__on_select)
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x * multiplier_2, y=hero_img_pos_y + new_line_y)

        load = Image.open(hero_mage)
        render = ImageTk.PhotoImage(load)
        img = Button(frame, image=render, bd=bd_size, command=self.__on_select)
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x * multiplier_3, y=hero_img_pos_y + new_line_y)

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
        opacity_slider.place(x=22, y=435)

    def __on_select(self):
        self.navigator.show(self.next_page)
