import tkinter
from tkinter import *
import random

class Raindrop:
    def __init__(self,tk_canvas: tkinter.Canvas):
        self.WINDOW = tk_canvas
        self.WIDTH = self.WINDOW.winfo_reqwidth()
        self.HEIGHT = self.WINDOW.winfo_reqheight()
        print(self.WIDTH, self.HEIGHT)
        self.x = 0
        self.y = self.HEIGHT
        self.speed = 1
        self.LENGTH = 10
        self.WINDOW.create_line(self.x, self.y, self.x, self.y+10)

        #DRAW THE RAINDROP ON THE CANVAS
    def fall(self):
            self.WINDOW.create_line(self.x, self.y, self.x, self.y - 10)
            self.y = self.y + 10 - self.LENGTH
            self.WINDOW.update()





#TESTING
root = Tk()
root.geometry("400x400")

c = Canvas(root)

r = Raindrop(c)

for _ in range(100):
    root.after(1000, r.fall)

c.pack()

root.mainloop()



