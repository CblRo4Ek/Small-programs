from tkinter import *
import random

class Pole(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=600, height=600, bg='black')
        self.canvas.pack()
        self.center = [300, 300]
        self.bind('<Double-ButtonPress-1>', self.press)
        self.stars = []
        self.sp = 8
        self.scale = Scale(self, from_ = 1, to = 25, label="Скорость", orient = 'horizontal',  command = self.speed)
        self.scale.set(self.sp)
        self.scale.pack()

    def create_star(self):
        for i in range(80):
            x = random.randint(self.center[0] - 350, self.center[0] + 350)
            y = random.randint(self.center[-1] - 350, self.center[-1] + 350)
            if abs(self.center[0] - x) < 150 and abs(self.center[-1] - y) < 150:
                size = 1
            elif 150 <= abs(self.center[0] - x) < 350 and 150 <= abs(self.center[-1] - y) < 350:
                size = 1.5
            elif 350 <= abs(self.center[0] - x) < 450 and 350 <= abs(self.center[-1] - y) < 450:
                size = 2
            elif 450 <= abs(self.center[0] - x) < 550 and 450 <= abs(self.center[-1] - y) < 550:
                size = 2.5
            else:
                size = 0
            star = self.canvas.create_oval(x, y, x + size, y + size, fill='white', outline="")
            self.stars.append(star)
        root.after(250, self.create_star)

    def fly_stars(self):
        for star in self.stars:
            x1, y1, x2, y2 = self.canvas.coords(star)
            if x1 > 600 or y1 > 600 or x2 < 0 or y2 < 0:
                self.canvas.delete(star)
                self.stars.remove(star)
                continue
            if x1 > 0 and y1 > 0:
                size = [(x1-self.center[0]) / x1, (y1-self.center[-1]) / y1]
            else:
                size = [0.98, 0.98]
            if x1 >= self.center[0] and y1 >= self.center[-1]:
                self.canvas.coords(star, x1 + size[0], y1 + size[-1], x2 + size[0] + 0.02, y2 + size[-1] + 0.02)
            elif x1 >= self.center[0] and y1 < self.center[-1]:
                self.canvas.coords(star, x1 + size[0], y1 + size[-1], x2 + size[0] + 0.02, y2 + size[-1] - 0.02)
                #self.canvas.coords(star, x1 + 1, y1 - size, x2 + size, y2 - 1)
            elif x1 < self.center[0] and y1 >= self.center[-1]:
                self.canvas.coords(star, x1 + size[0] - 0.02, y1 + size[-1], x2 + size[0], y2 + size[-1] + 0.02)
                #self.canvas.coords(star, x1 - size, y1 + 1, x2 - 1, y2 + size)
            else:
                self.canvas.coords(star, x1 + size[0] - 0.02, y1 + size[-1] - 0.02, x2 + size[0], y2 + size[-1])
                #self.canvas.coords(star, x1 - size, y1 - size, x2 - 1, y2 - 1)
        root.after(self.sp, self.fly_stars)

    def press(self, event):
        if event.x in range(0, 601) and event.y in range(0, 601):
            self.create_star()
            self.center = [event.x, event.y]

    def speed(self, val):
        self.sp = val

root = Pole()
root.fly_stars()
root.mainloop()