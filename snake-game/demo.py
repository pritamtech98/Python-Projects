from tkinter import *
import tkinter.ttk
import time
import threading
import random

def start():

    root = Tk()
    mainFrame(root)
    root.mainloop()

def snake_start(master):
    master.snake = snake(master.canvas)



def torgb(rgb):

    return "#%02x%02x%02x" % rgb


class mainFrame(Frame):

    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.master.title("Snake Game")
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.canvas = Canvas(self, width= 800, height= 600)
        self.canvas.config(bg = torgb((63, 62, 61)))
        self.canvas.focus_set()
        self.canvas.pack(side = "left")
        snake_thread = threading.Thread(target = lambda : snake_start(self))
        snake_thread.setDaemon(True)
        snake_thread.start()

class snake:

    def __init__(self, master):
        self.master = master
        self.x = 0
        self.y = 0
        while(1):
            fx = random.randrange(600) - 15 ; fy = random.randrange(800) - 15
            self.foodx = fx - divmod(fx, 15)[1]
            self.foody = fy - divmod(fy, 15)[1]
            if(self.foodx < 0 or self.foody < 0 or self.foodx + 15 > 800 or self.foody + 15 > 600):
                continue
            else:
                break

        self.speedx = 15
        self.speedy = 0
        self.rect = self.master.create_rectangle(0, 0, 15, 15)
        self.master.bind("<Key>", self.update)
        self.move_thread = threading.Thread(target=self.move)
        self.move_thread.setDaemon(True)
        self.move_thread.start()

    def move(self):

        self.x += self.speedx
        self.y += self.speedy
        self.show()

    def food(self):

        try:
            self.master.delete(self.foodpos)
        except:
            pass

        if((self.x <= self.foodx and self.x + 15 >= self.foodx and self.y <= self.foody and self.y + 15 >= self.foody) or
                (self.x >= self.foodx and self.x <= self.foodx + 15 and self.y <= self.foody and self.y + 15 >= self.foody) or
                (self.x <= self.foodx and self.x + 15 >= self.foodx and self.y >= self.foody and self.y <= self.foody + 15) or
                (self.x >= self.foodx and self.x <= self.foodx + 15 and self.y >= self.foody and self.y <= self.foody + 15)):
            while (1):
                fx = random.randrange(600) - 15
                fy = random.randrange(800) - 15
                self.foodx = fx - divmod(fx, 15)[1]
                self.foody = fy - divmod(fy, 15)[1]
                if (self.foodx < 0 or self.foody < 0 or self.foodx > 800 or self.foody > 600):
                    continue
                else:
                    break
        self.foodpos = self.master.create_rectangle(self.foodx, self.foody, self.foodx+15, self.foody+15, fill="red")

    def update(self, event):

        if (event.keycode == 37):
            self.speedx = -15
            self.speedy = 0
        elif (event.keycode == 39):
            self.speedx = 15
            self.speedy = 0
        elif (event.keycode == 38):
            self.speedx = 0
            self.speedy = -15
        elif (event.keycode == 40):
            self.speedx = 0
            self.speedy = 15


    def show(self):
        self.master.delete(self.rect)
        self.rect = self.master.create_rectangle(self.x, self.y, self.x + 15, self.y + 15, fill="white")
        self.food()
        time.sleep(.23)
        self.move()



myThread = threading.Thread(target=start)
myThread.start()