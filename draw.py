from tkinter import *
import math

class Draw:
    def __init__(self, master, canvas_reqheight, canvas_reqwidth):
        self.w = Canvas(master, width=canvas_reqwidth, height=canvas_reqheight)
        self.w.grid()

    def draw_regular_polygon(self, center, radius, n, angle, **kwargs):
        angle -= (math.pi / n)
        coord_list = [[center[0] + radius * math.sin((2 * math.pi / n) * i - angle),
                       center[1] + radius * math.cos((2 * math.pi / n) * i - angle)] for i in range(n)]
        return self.w.create_polygon(coord_list, **kwargs)
