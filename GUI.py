import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Window properties
hero_size = "520x540"
build_size = "320x198"
bg_image_hero = "assets/image/backgrounds/background_hero.png"
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

# Slider properties
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


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack()

        self.frames = {}

        for F in (PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=origin, column=origin, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]

        # Raises the shown container to the top
        frame.tkraise()

        # Adjusts the window size to fit the raised container
        if cont == PageOne:
            Window.wm_geometry(self, hero_size)
        else:
            Window.wm_geometry(self, build_size)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open(bg_image_hero)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, bd=bd_size)
        img.image = render
        img.grid(row=origin, column=origin)

        # Hero roster
        banner_hero = Label(self, text=banner_hero_txt, fg=txt_color, bg=default_color, width=txt_width,
                            font=(txt_font, txt_size, txt_type))
        banner_hero.place(x=txt_pos_x, y=txt_pos_y)

        load = Image.open(hero_tank)
        render = ImageTk.PhotoImage(load)
        img = Button(self, image=render, bd=bd_size, command=lambda: controller.show_frame(PageTwo))
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x, y=hero_img_pos_y + new_line_y)

        load = Image.open(hero_agility)
        render = ImageTk.PhotoImage(load)
        img = Button(self, image=render, bd=bd_size, command=lambda: controller.show_frame(PageTwo))
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x * multiplier_2, y=hero_img_pos_y + new_line_y)

        load = Image.open(hero_mage)
        render = ImageTk.PhotoImage(load)
        img = Button(self, image=render, bd=bd_size, command=lambda: controller.show_frame(PageTwo))
        img.image = render
        img.place(x=hero_img_pos_x + new_line_x * multiplier_3, y=hero_img_pos_y + new_line_y)

        # Settings
        banner_settings = Label(self, text=banner_settings_txt, fg=txt_color, bg=default_color, width=txt_width,
                                font=(txt_font, txt_size, txt_type))
        banner_settings.place(x=txt_pos_x, y=txt_pos_y + txt_new_line_y)

        # UI settings labels
        ui_txt_def = Label(self, text=ui_def_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_def.place(x=ui_txt_pos_x, y=ui_txt_pos_y)

        ui_txt_win = Label(self, text=ui_win_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_win.place(x=ui_txt_pos_x + ui_new_line_x, y=ui_txt_pos_y)

        ui_txt_vet = Label(self, text=ui_vet_txt, fg=txt_color, bg=default_color, width=ui_txt_width,
                           font=(txt_font, settings_txt_size, txt_type))
        ui_txt_vet.place(x=ui_txt_pos_x + ui_new_line_x * multiplier_2, y=ui_txt_pos_y)

        ui_slider = Scale(self, from_=min_ui, to=max_ui, length=slider_bar_length, orient=HORIZONTAL, bd=bd_size,
                          sliderlength=slider_length, showvalue=slider_no_value, resolution=ui_slider_res)
        ui_slider.place(x=22, y=371)

        occlusion_label = Label(self, text=opacity_txt, fg=txt_color, bg=default_color, width=38,
                                font=(txt_font, settings_txt_size, txt_type))
        occlusion_label.place(x=txt_pos_x, y=404)

        # Change of opacity function with the slider value 'a'
        def alpha(a):
            app.attributes('-alpha', a)

        opacity_slider = Scale(self, from_=min_opacity, to=max_opacity, length=slider_bar_length, orient=HORIZONTAL,
                               bd=bd_size, sliderlength=slider_length, showvalue=slider_no_value,
                               resolution=opacity_slider_res, command=alpha)
        opacity_slider.place(x=22, y=435)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open(bg_image_build)
        render = ImageTk.PhotoImage(load)
        img_bg = Label(self, image=render, bd=bd_size)
        img_bg.image = render
        img_bg.grid(row=origin, column=origin)

        # Hero image and return button
        load = Image.open(selected_hero)
        render = ImageTk.PhotoImage(load)
        img_hero = Button(self, image=render, bd=bd_size, command=lambda: controller.show_frame(PageOne))
        img_hero.image = render
        img_hero.place(x=origin, y=origin)

        # Abilities for build
        load = Image.open(img_1)
        render = ImageTk.PhotoImage(load)
        item_1 = Label(self, image=render, bg=highlight_color)
        item_1.image = render
        item_1.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y)

        load = Image.open(img_2)
        render = ImageTk.PhotoImage(load)
        item_2 = Label(self, image=render, bg=highlight_color)
        item_2.image = render
        item_2.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_2)

        load = Image.open(img_3)
        render = ImageTk.PhotoImage(load)
        item_3 = Label(self, image=render, bg=highlight_color)
        item_3.image = render
        item_3.place(x=img_pos_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_3)

        load = Image.open(img_4)
        render = ImageTk.PhotoImage(load)
        item_4 = Label(self, image=render, bg=highlight_color)
        item_4.image = render
        item_4.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y)

        load = Image.open(img_5)
        render = ImageTk.PhotoImage(load)
        item_5 = Label(self, image=render, bg=highlight_color)
        item_5.image = render
        item_5.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_2)

        load = Image.open(img_6)
        render = ImageTk.PhotoImage(load)
        item_6 = Label(self, image=render, bg=highlight_color)
        item_6.image = render
        item_6.place(x=img_pos_x + new_img_line_x + new_img_line_x, y=img_pos_y + new_img_line_y * multiplier_3)


app = Window()
app.resizable(False, False)
app.mainloop()
