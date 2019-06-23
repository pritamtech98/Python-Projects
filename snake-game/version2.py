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

    snakes = []

    def __init__(self, master):
        self.master = master
        self.coord = [[0, 0]]
        while(1):
            fx = random.randrange(600) - 15 ; fy = random.randrange(800) - 15
            self.foodx = fx - divmod(fx, 15)[1]
            self.foody = fy - divmod(fy, 15)[1]
            if(self.foodx < 0 or self.foody < 0 or self.foodx + 15 > 800 or self.foody + 15 > 600):
                continue
            else:
                break

        self.speed = [[15, 0]]
        self.rect = [self.master.create_rectangle(self.coord[0][0], self.coord[0][1], 15, 15)]
        self.master.bind("<Key>", self.update)
        self.move_thread = threading.Thread(target=self.move)
        self.move_thread.setDaemon(True)
        self.change_coordx = []
        self.change_coordy = []
        self.change_speedx = []
        self.change_speedy = []
        self.change_pos = []
        self.move_thread.start()


    def move(self):

        for i in range(len(self.rect)-1, -1, -1):
            # for el in range(len(self.change_pos)):
            #     if(self.change_pos[el] >= 0):
            #         if(self.coord[i][0] == self.change_coordx[el] and self.coord[i][1] == self.change_coordy[el]):
            #             self.speed[self.change_pos[el]][0] = self.change_speedx[el]
            #             self.speed[self.change_pos[el]][1] = self.change_speedy[el]
            #             self.change_pos[el] -= 1
            self.coord[i][0] += self.speed[i][0]
            self.coord[i][1] += self.speed[i][1]
        self.show()


    def food(self):

        try:
            self.master.delete(self.foodpos)
        except:
            pass

        if((self.coord[-1][0] <= self.foodx and self.coord[-1][0] + 15 >= self.foodx and self.coord[-1][1] <= self.foody and self.coord[-1][1] + 15 >= self.foody) or
                (self.coord[-1][0] >= self.foodx and self.coord[-1][0] <= self.foodx + 15 and self.coord[-1][1] <= self.foody and self.coord[-1][1] + 15 >= self.foody) or
                (self.coord[-1][0] <= self.foodx and self.coord[-1][0] + 15 >= self.foodx and self.coord[-1][1] >= self.foody and self.coord[-1][1] <= self.foody + 15) or
                (self.coord[-1][0] >= self.foodx and self.coord[-1][0] <= self.foodx + 15 and self.coord[-1][1] >= self.foody and self.coord[-1][1] <= self.foody + 15)):

            while (1):
                prevx = self.coord[-1][0]
                prevy = self.coord[-1][1]
                prev_speedx = self.speed[-1][0]
                prev_speedy = self.speed[-1][1]
                self.coord[-1][0] += prev_speedx
                self.coord[-1][1] += prev_speedy
                self.rect.insert(0, self.master.create_rectangle(prevx, prevy, 15, 15, fill="white"))
                self.coord.insert(0, [prevx, prevy])
                self.speed.insert(0, [prev_speedx, prev_speedy])
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
            self.speed[-1][0] = -15
            self.speed[-1][1] = 0
            if (len(self.rect) > 1):
                self.change_coordx.append(self.coord[-1][0])
                self.change_coordy.append(self.coord[-1][1])
                self.change_speedx.append(self.speed[-1][0])
                self.change_speedy.append(self.speed[-1][1])
                self.change_pos.append(len(self.rect) - 2)
        elif (event.keycode == 39):
            self.speed[-1][0] = 15
            self.speed[-1][1] = 0
            if (len(self.rect) > 1):
                self.change_coordx.append(self.coord[-1][0])
                self.change_coordy.append(self.coord[-1][1])
                self.change_speedx.append(self.speed[-1][0])
                self.change_speedy.append(self.speed[-1][1])
                self.change_pos.append(len(self.rect) - 2)
        elif (event.keycode == 38):
            self.speed[-1][0] = 0
            self.speed[-1][1] = -15
            if (len(self.rect) > 1):
                self.change_coordx.append(self.coord[-1][0])
                self.change_coordy.append(self.coord[-1][1])
                self.change_speedx.append(self.speed[-1][0])
                self.change_speedy.append(self.speed[-1][1])
                self.change_pos.append(len(self.rect) - 2)
        elif (event.keycode == 40):
            self.speed[-1][0] = 0
            self.speed[-1][1] = 15
            if (len(self.rect) > 1):
                self.change_coordx.append(self.coord[-1][0])
                self.change_coordy.append(self.coord[-1][1])
                self.change_speedx.append(self.speed[-1][0])
                self.change_speedy.append(self.speed[-1][1])
                self.change_pos.append(len(self.rect) - 2)

    def show(self):
        for i in range(len(self.rect)):
            self.master.delete(self.rect[i])
        for i in range(len(self.rect)):
            self.rect[i] = self.master.create_rectangle(self.coord[i][0], self.coord[i][1], self.coord[i][0] + 15, self.coord[i][1] + 15, fill="white")
        self.food()
        time.sleep(.2)
        self.move()



myThread = threading.Thread(target=start)
myThread.start()