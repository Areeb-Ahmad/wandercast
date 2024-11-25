#!/usr/bin/env

import tkinter as tk
from tkinter import *
import random

root = tk.Tk()


WIDTH = 400
HEIGHT = 400

c = Canvas(root, width = WIDTH, height = HEIGHT)
c.pack()

y = 0

for _ in range(100):
	y += 10
	c.create_line(50,y,50, y+10)
	root.update()

root.mainloop()
