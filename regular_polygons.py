# -------------------------
# EASTER EGG:
# import this

# -------------------------
# grid manager
from tkinter import *
from tkinter import colorchooser
import draw

# -------------------------
# GUI
menuMain = Tk()
menuMain.iconbitmap(default="images/transparent.ico")
menuMain.title("Regular Polygons")
menuMain.geometry("485x432")
menuMain['bg'] = '#f0f0f0'

# -------------------------
# VARIABLES and CONSTANTS

# SCREEN
canvas_reqheight = 362
canvas_reqwidth = 465

# SIDES
default_sides = StringVar(value="5")
value_sides = StringVar(value="5")
min_sides = 3
max_sides = 15

# RADIUS - EXPERIMENTAL
# default_radius = StringVar(value="100")
# value_radius = StringVar(value="100")
# min_radius = 1
# max_radius = 360

# ANGLE
default_angle = StringVar(value="18")
value_angle = StringVar(value="18")
min_angle = 1
max_angle = 360

# COLOR
default_color = StringVar(value="#ff0000")
value_color = StringVar(value="#ff0000")

# WIDTH
default_width = StringVar(value="100")
value_width = StringVar(value="100")
min_width = 1
max_width = 200


# -------------------------
# Class
class MenuMain:
    def __init__(self):
        _MenuFrame(menuMain)
        _ButtonFrame(menuMain)


class _MenuFrame:
    def __init__(self, master):
        # -------------------------
        # widgets
        menu_frame = Frame(master)

        # -------------------------
        Label(menu_frame,
              text="Sides:",
              font="MicrosoftSansSerif 8"
              ).grid(row=0, column=0, padx=7, pady=7, sticky=NW)

        Label(menu_frame,
              text="Radius:",
              font="MicrosoftSansSerif 8"
              ).grid(row=0, column=1, padx=2, pady=7, sticky=NW)

        Label(menu_frame,
              text="Angle:",
              font="MicrosoftSansSerif 8"
              ).grid(row=0, column=2, padx=5, pady=7, sticky=NW)

        Label(menu_frame,
              text="Color:",
              font="MicrosoftSansSerif 8",
              ).grid(row=0, column=3, padx=1, pady=7, sticky=NW)

        Label(menu_frame,
              text="Width:",
              font="MicrosoftSansSerif 8"
              ).grid(row=0, column=4, padx=1, pady=7, sticky=NW)

        # -------------------------
        # menu_frame - row = 1

        self.sb_sides = Spinbox(
            menu_frame,
            from_=min_sides,
            to=max_sides,
            textvariable=value_sides,
            wrap=True,
            state=NORMAL,
            width=5)

        # EXPERIMENTAL:
        # self.sb_radius = Spinbox(
        #     menu_frame,
        #     from_=min_radius,
        #     to=max_radius,
        #     textvariable=value_radius,
        #     wrap=True,
        #     state=NORMAL,
        #     width=5)

        self.sb_angle = Spinbox(
            menu_frame,
            from_=min_angle,
            to=max_angle,
            textvariable=value_angle,
            wrap=True,
            state=NORMAL,
            width=5)

        self.lbl_color = Label(menu_frame,
                               text="",
                               font="MicrosoftSansSerif 8",
                               cursor="hand2",
                               bg=value_color.get(),
                               fg="#ffffff",
                               width=8
                               )

        self.sb_width = Spinbox(
            menu_frame,
            from_=min_width,
            to=max_width,
            textvariable=value_width,
            wrap=True,
            state=NORMAL,
            width=5)

        # -------------------------
        # layout

        self.sb_sides.grid(row=1, column=0, padx=8, pady=0, sticky=NW)
        # EXPERIMENTAL:
        #self.sb_radius.grid(row=1, column=1, padx=3, pady=0, sticky=NW)
        self.sb_angle.grid(row=1, column=2, padx=6, pady=0, sticky=NW)

        self.lbl_color.grid(row=1, column=3, padx=3, pady=0, sticky=NW)
        self.lbl_color.bind('<Button-1>', self.choose_color, value_color)

        self.sb_width.grid(row=1, column=4, padx=3, pady=0, sticky=NW)

        menu_frame.grid(row=0, column=0)

    @staticmethod
    def choose_color(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title="Choose color")
        value_color.set(color_code[1])
        mc = _MenuFrame(menuMain)
        ch_color = value_color.get()
        mc.set_muda_cor_label(ch_color)

    # Setter
    def set_muda_cor_label(self, cor):
        self.lbl_color.config(bg=cor)


class _ButtonFrame:
    def __init__(self, master):
        # -------------------------
        # widgets
        button_frame = Frame(master)

        btn_draw = Button(button_frame, text="Draw TKINTER", bg="#e1e1e1", padx=10, pady=5,
                          command=self._button_frame_click)

        btn_draw.grid(row=0, column=5, padx=98, pady=5, sticky=NW)
        btn_draw.focus()

        button_frame.grid(row=0, column=1)

    def _button_frame_click(self):
        # -----------------------------------
        # Check that the data is valid
        self._val_sb_sides()
        # EXPERIMENTAL:
        #self._val_sb_radius(value_radius.get())
        self._val_sb_angle()
        self._val_sb_width()
        # -----------------------------------
        half_reqheight = canvas_reqheight / 2
        half_reqwidth = canvas_reqwidth / 2

        sides = int(value_sides.get())
        # EXPERIMENTAL:
        #radius = int(value_radius.get())
        angle = int(value_angle.get())
        color = value_color.get()
        width = int(value_width.get())

        menu_canvas = Frame(menuMain)
        dr = draw.Draw(menu_canvas, canvas_reqheight, canvas_reqwidth)
        dr.draw_regular_polygon((half_reqwidth, half_reqheight), width, sides, angle, fill=color, outline=color)
        menu_canvas.grid(row=2, column=0, padx=1, pady=1, columnspan=2, sticky=W)

    @staticmethod
    def _val_sb_sides():
        # check value is integer
        # check if is NOT in range
        try:
            if int(value_sides.get()) not in range(min_sides, max_sides + 1):
                value_sides.set(default_sides.get())
        except ValueError:
            # Handle the exception - return to default value
            value_sides.set(default_sides.get())

    # # EXPERIMENTAL:
    # @staticmethod
    # def _val_sb_radius(val):
    #     mf = _MenuFrame(menuMain)
    #
    #     # get minimum and maximum values of the widget to be validated
    #     min_val = int(mf.sb_radius.config('from')[4])
    #     max_val = int(mf.sb_radius.config('to')[4]) + 1
    #
    #     # ---------------------------------------------------
    #     # print(f'\nValue Radius origin: {val}')
    #     # print(f'Value Radius change: {value_radius.get()}')
    #     # print(f'Min Radius: {min_val}')
    #     # print(f'Max Radius: {max_val - 1}')
    #     # print(f"Val: {val} NOT IN Min: {min_val}, Max: {max_val - 1}")
    #     # ---------------------------------------------------
    #
    #     # check value is integer
    #     # check if is NOT in range
    #     try:
    #         if int(val) not in range(min_val, max_val):
    #             value_radius.set(default_radius.get())
    #     except ValueError as e:
    #         # Handle the exception - return to default value
    #         value_radius.set(default_radius.get())
    #         print(type(e))  # the exception type
    #         print(e.args)  # arguments stored in .args
    #         e.__setstate__(None)

    @staticmethod
    def _val_sb_angle():
        # check value is integer
        # check if is NOT in range
        try:
            if int(value_angle.get()) not in range(min_angle, max_angle + 1):
                value_angle.set(default_angle.get())
        except ValueError:
            # Handle the exception - return to default value
            value_angle.set(default_angle.get())

    @staticmethod
    def _val_sb_width():
        # check value is integer
        # check if is NOT in range
        try:
            if int(value_width.get()) not in range(min_width, max_width + 1):
                value_width.set(default_width.get())
        except ValueError:
            # Handle the exception - return to default value
            value_width.set(default_width.get())


# -------------------------
# Screen
MenuMain()
menuMain.mainloop()
