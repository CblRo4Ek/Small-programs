from tkinter import *
import random

class Pole(Tk):
    def __init__(self):
        super().__init__()
        self.title('Фейерверки')
        self.canvas = Canvas(self, width=850, height=650, bg='black')
        self.canvas.pack()
        self.points = []
        self.colors = ['red', 'blue', 'green', 'yellow', 'white', 'pink', 'azure', 'brown', 'aquamarine']

    def detonation(self):
        for firework in self.points:
            if len(firework) == 2:
                if firework[-1] == 22:
                    for i in firework[0]:
                        self.canvas.delete(i[0])
                    self.points.remove(firework)
                else:
                    for point in firework[0]:
                        point[-1] += 1
                        x1, y1, x2, y2 = self.canvas.coords(point[0])
                        if point[-1] % 8 == 0:
                            point[-1] -= 1
                            self.canvas.coords(point[0], x1, y1 + 2, x2, y2 + 2)
                        elif point[-1] < 24:
                            self.canvas.coords(point[0], x1 + self.r(2), y1 - self.r(), x2 + self.r(2), y2 - self.r())
                        elif 24 <= point[-1] < 48:
                            self.canvas.coords(point[0],  x1 + self.r(), y1 - self.r(2), x2 + self.r(), y2 - self.r(2))
                        elif 48 <= point[-1] < 72:
                            self.canvas.coords(point[0], x1 - self.r(), y1 - self.r(2), x2 - self.r(), y2 - self.r(2))
                        elif 72 <= point[-1] < 96:
                            self.canvas.coords(point[0],  x1 - self.r(2), y1 - self.r(), x2 - self.r(2), y2 - self.r())
                        elif 96 <= point[-1] < 120:
                            self.canvas.coords(point[0], x1 - self.r(2), y1 + self.r(), x2 - self.r(2), y2 + self.r())
                        elif 120 <= point[-1] < 144:
                            self.canvas.coords(point[0],  x1 - self.r(), y1 + self.r(2), x2 - self.r(), y2 + self.r(2))
                        elif 144 <= point[-1] < 168:
                            self.canvas.coords(point[0], x1 + self.r(), y1 + self.r(2), x2 + self.r(), y2 + self.r(2))
                        else:
                            self.canvas.coords(point[0],  x1 + self.r(2), y1 + self.r(), x2 + self.r(2), y2 + self.r())
                firework[-1] += 1
            else:
                x1, y1, x2, y2 = self.canvas.coords(firework[0])
                if y1 <= firework[-1]:
                    self.create_detonation(firework[1], x1, y1, x2, y2)
                    self.canvas.delete(firework[0])
                    self.points.remove(firework)
                else:
                    self.canvas.coords(firework[0], x1, y1 - 10, x2, y2 - 10)
                    firework[-1] += 2
        if random.randint(0, 10) == 10:
            x = random.randint(0, 850)
            color = random.choice(self.colors)
            self.points += [[self.canvas.create_oval(x, 650, x + 5, 655, fill=color, outline=""), color, random.randint(5, 500)]]
        root.after(50, self.detonation)

    def create_detonation(self, color, x1, y1, x2, y2):
        self.points += [[[[self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=""), i] for i in range(192)], 1]]

    def r(self, x = 1):
        return random.randint(6, 8) * x
root = Pole()
root.detonation()
root.mainloop()