from tkinter import *
import random
from math import sin, cos, radians

class Pole(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=850, height=650, bg='black')
        self.canvas.pack()
        self.flyes = []
        self.points = []
        self.colors = ['red', 'blue', 'green', 'yellow', 'pink']

    def detonation(self):
        #print(points)
        for firework in self.points:
            if len(firework) == 2:
                if firework[-1] == 35:
                    for i in firework[0]:
                        self.canvas.delete(i[0])
                    self.points.remove(firework)
                else:
                    #print(firework)
                    for point in firework[0]:
                        #print(point)
                        x1, y1, x2, y2 = self.canvas.coords(point[0])
                        r = random.randint(1, 7)
                        if point[-1] % 90 <= 4:
                            self.canvas.coords(point[0], x1, y1 + 2, x2, y2 + 2)
                        elif 270 < point[-1] <= 305:
                            self.canvas.coords(point[0], x1 + 1.2*r, y1 + 2*r, x2 + 1.2*r, y2 + 2*r)
                            point[-1] -= 5
                        elif 305 < point[-1] < 360:
                            self.canvas.coords(point[0],  x1 + cos(radians(point[-1]))*r, y1 + sin(radians(point[-1]))*r, x2 + cos(radians(point[-1]))*r, y2 + sin(radians(point[-1]))*r)
                            point[-1] -= 5
                        elif 360 < point[-1] <= 400:
                            self.canvas.coords(point[0], x1 + 1.5*r, y1 - 2*r, x2 + 1.5*r, y2 - 2*r)
                            point[-1] -= 5
                        elif 400 < point[-1] < 450:
                            self.canvas.coords(point[0], x1 + cos(radians(point[-1]))*r, y1 + sin(radians(point[-1]))*r, x2 + cos(radians(point[-1]))*r, y2 + sin(radians(point[-1]))*r)
                            point[-1] -= 5
                        elif 450 < point[-1] <= 490:
                            self.canvas.coords(point[0], x1 + cos(radians(point[-1]))*r, y1 + sin(radians(point[-1]))*r, x2 + cos(radians(point[-1]))*r, y2 + sin(radians(point[-1]))*r)
                            point[-1] -= 5
                        elif 490 < point[-1] <= 540:
                            self.canvas.coords(point[0], x1 - 1.5*r, y1 - 2*r, x2 - 1.5*r, y2 - 2*r)
                            point[-1] -= 5
                        elif 540 < point[-1] <= 580:
                            self.canvas.coords(point[0], x1 + cos(radians(point[-1]))*r, y1 + sin(radians(point[-1]))*r, x2 + cos(radians(point[-1]))*r, y2 + sin(radians(point[-1]))*r)
                            point[-1] -= 5
                        else:
                            self.canvas.coords(point[0], x1 - 1.2*r, y1 + 2*r, x2 - 1.2*r, y2 + 2*r)
                            point[-1] += 5

                firework[-1] += 1
            else:
                #print(firework)
                x1, y1, x2, y2 = self.canvas.coords(firework[0])
                if y1 <= firework[-1]:
                    self.create_detonation(firework[1], x1, y1, x2, y2)
                    self.canvas.delete(firework[0])
                    self.points.remove(firework)
                else:
                    self.canvas.coords(firework[0], x1, y1 - 9, x2, y2 - 9)
                    firework[-1] += 2
        if random.randint(0, 10) == 10:
            x = random.randint(0, 850)
            color = random.choice(self.colors)
            self.points += [[self.canvas.create_oval(x, 650, x + 5, 655, fill=color, outline=""), color, random.randint(5, 500)]]
        root.after(50, self.detonation)

    def create_detonation(self, color, x1, y1, x2, y2):
        self.points += [[[[self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=""), 270 + int(2.1*i)] for i in range(170)], 1]]


    '''def fly(self):
        for point in self.flyes:
            x1, y1, x2, y2 = self.canvas.coords(point[0])
            if y1 <= point[-1]:
                self.create_detonation(point[1], x1, y1, x2, y2)
                self.canvas.delete(point[0])
                self.flyes.remove(point)
            else:
                self.canvas.coords(point[0], x1, y1 - 2, x2, y2 - 2)
                point[-1] += 2
        root.after(50, self.fly)'''

'''    def create_fly(self):
        x = random.randint(0, 850)
        color = random.choice(self.colors)
        self.points += [[self.canvas.create_oval(x, 650, x + 7, 657, fill=color, outline=""), color, random.randint(5, 500)]]
        #print(self.points)
        self.detonation()

    def create_fly_auto(self):
        x = random.randint(0, 850)
        color = random.choice(self.colors)
        self.points += [[self.canvas.create_oval(x, 650, x + 7, 657, fill=color, outline=""), color, random.randint(5, 500)]]
        #print(self.points)
        self.detonation()
        root.after(350, self.create_fly_auto)'''


root = Pole()
root.detonation()
root.mainloop()