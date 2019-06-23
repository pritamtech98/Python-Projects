from tkinter import *
import tkinter.ttk
from PIL import Image, ImageTk
import time
import tkinter.messagebox
import threading

class loginFrame(Frame):

    def __init__(self, master):
        self.master=master
        super().__init__(master)
        self.master.title("Login")
        self.pack()
        self.createwidget()

    def window_on_delete(self):
        val = tkinter.messagebox.askokcancel("Quit", "Do you really want to quit the game?")
        if (val):
            self.top.destroy()
            self.master.deiconify()

    def action_start(self):
        self.master.iconify()
        self.top=Toplevel()
        self.top.protocol("WM_DELETE_WINDOW", self.window_on_delete)
        mainFrame(self.top, [self.frame1.var_name.get(), self.frame1.var_age.get(), self.frame1.var_email.get()], [self.frame2.var_name.get(), self.frame2.var_age.get(), self.frame2.var_email.get()], int(self.container_frame.combo_round.get()))

    def combo_listener(self, event):
        pass

    def createwidget(self):

        self.heading_frame=Frame(self, bg='grey')
        self.heading_frame.pack(pady=10, padx=8)
        self.heading_frame.lbl=Label(self.heading_frame, text="Welcome to my tic-tac-toe game", font='arial 20 bold italic', bg='light grey', fg='grey')
        self.heading_frame.lbl.pack(pady=4, padx=3)

        self.container_frame=Frame(self, bg='#D5D5D5')
        self.container_frame.pack(pady=20)
        self.frame1=LabelFrame(self.container_frame, text="Player 1", fg='grey', bg='#EAEAEA')
        self.frame2=LabelFrame(self.container_frame, text="Player 2", fg='grey', bg='#EAEAEA')
        self.frame1.grid(row=0, column=0, padx=16, pady=4)
        self.frame2.grid(row=0, column=1, padx=16, pady=4)

        self.frame1.lbl_name=Label(self.frame1, text="Name : ", anchor=W, font='arial 10 bold')
        self.frame1.lbl_age=Label(self.frame1, text="Age : ", anchor=W, font='arial 10 bold')
        self.frame1.lbl_email=Label(self.frame1, text="Email Id : ", anchor=W, font='arial 10 bold')
        self.frame1.lbl_name.grid(row=0, column=0, padx=4, pady=8)
        self.frame1.lbl_age.grid(row=1, column=0, padx=4, pady=8)
        self.frame1.lbl_email.grid(row=2, column=0, padx=4, pady=8)
        self.frame1.var_name=StringVar()
        self.frame1.var_age=IntVar()
        self.frame1.var_email=StringVar()
        self.frame1.ent_name=tkinter.ttk.Entry(self.frame1, width=22, textvariable=self.frame1.var_name)
        self.frame1.ent_name.grid(row=0, column=1, padx=9)
        self.frame1.ent_age = tkinter.ttk.Entry(self.frame1, width=22, textvariable=self.frame1.var_age)
        self.frame1.ent_age.grid(row=1, column=1, padx=9)
        self.frame1.ent_email = tkinter.ttk.Entry(self.frame1, width=22, textvariable=self.frame1.var_email)
        self.frame1.ent_email.grid(row=2, column=1, padx=9)
        self.frame1.var_chk1=IntVar()
        self.frame2.var_chk2=IntVar()
        self.frame1.btn_submit=tkinter.ttk.Checkbutton(self.frame1, text="All filled", variable=self.frame1.var_chk1, onvalue=1, offvalue=0)
        self.frame1.btn_submit.grid(columnspan=2, pady=30)

        self.frame2.lbl_name = Label(self.frame2, text="Name : ", anchor=W, font='arial 10 bold')
        self.frame2.lbl_age = Label(self.frame2, text="Age : ", anchor=W, font='arial 10 bold')
        self.frame2.lbl_email = Label(self.frame2, text="Email Id : ", anchor=W, font='arial 10 bold')
        self.frame2.lbl_name.grid(row=0, column=0, padx=4, pady=8)
        self.frame2.lbl_age.grid(row=1, column=0, padx=4, pady=8)
        self.frame2.lbl_email.grid(row=2, column=0, padx=4, pady=8)
        self.frame2.var_name = StringVar()
        self.frame2.var_age = IntVar()
        self.frame2.var_email = StringVar()
        self.frame2.ent_name = tkinter.ttk.Entry(self.frame2, width=22, textvariable=self.frame2.var_name)
        self.frame2.ent_name.grid(row=0, column=1, padx=9)
        self.frame2.ent_age = tkinter.ttk.Entry(self.frame2, width=22, textvariable=self.frame2.var_age)
        self.frame2.ent_age.grid(row=1, column=1, padx=9)
        self.frame2.ent_email = tkinter.ttk.Entry(self.frame2, width=22, textvariable=self.frame2.var_email)
        self.frame2.ent_email.grid(row=2, column=1, padx=9)
        self.frame2.btn_submit = tkinter.ttk.Checkbutton(self.frame2, text="All filled", variable=self.frame2.var_chk2,
                                                         onvalue=1, offvalue=0)
        self.frame2.btn_submit.grid(columnspan=2, pady=30)

        self.container_frame.lbl_round=Label(self.container_frame, text="No of rounds", font='arial 10 bold')
        self.container_frame.lbl_round.grid(row=1, column=0, pady=20)
        self.container_frame.combo_round = tkinter.ttk.Combobox(self.container_frame, width=11, value=[1, 3, 5, 7])
        self.container_frame.combo_round.set(1)
        self.container_frame.combo_round.bind("<<ComboboxSelected>>", self.combo_listener)
        self.container_frame.combo_round.grid(row=1, column=1, pady=20)
        self.container_frame.btn_start=tkinter.ttk.Button(self.container_frame, text="Start", width=50, padding=(10, 5), command=self.action_start)
        self.container_frame.btn_start.grid(columnspan=2, sticky=S, pady=10, padx=5)

class alert_frame(Frame):

    def __init__(self, master, winner):
        super().__init__(master)
        self.master=master
        master.title("Winner")
        self.pack()
        self.winner=winner
        self.createWidget()

    def createWidget(self):
        self.label_winner=Label(self, text="Winner", font='arial 20 bold')
        self.label_winner.pack(pady=20)
        self.label_winner_name=Label(self, text="Hurray !! "+self.winner+" is the winner", font='arial 15')
        self.label_winner_name.pack(pady=10, padx=40)

class mainFrame(Frame):

    event_log=[]
    row2 = 0
    row3 = 0
    col1 = 0
    col2 = 0
    col3 = 0
    row1 = 0
    diag1 = 0
    diag2 = 0
    row1data=[]; row2data=[]; row3data=[]; col1data=[]; col2data=[]; col3data=[]; diag1data=[]; diag2data=[]
    cur_round=1

    def __init__(self, master, player1, player2, no_of_rounds):
        super().__init__(master, bg='#BDBDBD')
        self.master=master
        self.player1=player1
        self.player2=player2
        self.no_of_rounds=no_of_rounds
        self.player1_score=0
        self.player2_score=0
        self.no_of_btn=0
        self.master.title("game")
        self.master.minsize(400, 300)
        self.pack()
        self.createWidget()

    def switch_turn(self):
        if(self.frame_turn.lbl_turn_player['text']==str(self.player1[0]).lower().capitalize()):
            self.frame_turn.lbl_turn_player['text']=str(self.player2[0]).lower().capitalize()
        else:
            self.frame_turn.lbl_turn_player['text'] = str(self.player1[0]).lower().capitalize()
        self.frame_turn.lbl_round['text']="Round : "+str(mainFrame.cur_round)

    def do_all_check(self):

        check_val=0

        if (mainFrame.row1 == 3):
            if (mainFrame.row1data[0] == mainFrame.row1data[1] == mainFrame.row1data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn1['text'] = '-'
                self.btn2['text'] = '-'
                self.btn3['text'] = '-'
                check_val+=1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()

        if (mainFrame.row2 == 3):
            if (mainFrame.row2data[0] == mainFrame.row2data[1] == mainFrame.row2data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn4['text'] = '-'
                self.btn5['text'] = '-'
                self.btn6['text'] = '-'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()
        if (mainFrame.row3 == 3):
            if (mainFrame.row3data[0] == mainFrame.row3data[1] == mainFrame.row3data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn7['text'] = '-'
                self.btn8['text'] = '-'
                self.btn9['text'] = '-'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()

        if (mainFrame.col1 == 3):
            if (mainFrame.col1data[0] == mainFrame.col1data[1] == mainFrame.col1data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn1['text'] = '|'
                self.btn4['text'] = '|'
                self.btn7['text'] = '|'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()
        if (mainFrame.col2 == 3):
            if (mainFrame.col2data[0] == mainFrame.col2data[1] == mainFrame.col2data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn2['text'] = '|'
                self.btn5['text'] = '|'
                self.btn8['text'] = '|'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()
        if (mainFrame.col3 == 3):
            if (mainFrame.col3data[0] == mainFrame.col3data[1] == mainFrame.col3data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn3['text'] = '|'
                self.btn6['text'] = '|'
                self.btn9['text'] = '|'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()
        if (mainFrame.diag1 == 3):
            if (mainFrame.diag1data[0] == mainFrame.diag1data[1] == mainFrame.diag1data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn1['text'] = '\\'
                self.btn5['text'] = '\\'
                self.btn9['text'] = '\\'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()
        if (mainFrame.diag2 == 3):
            if (mainFrame.diag2data[0] == mainFrame.diag2data[1] == mainFrame.diag2data[
                2] and mainFrame.cur_round <= self.no_of_rounds):
                self.btn3['text'] = '/'
                self.btn5['text'] = '/'
                self.btn7['text'] = '/'
                check_val += 1
                tkinter.messagebox.showinfo("Winner", self.frame_turn.lbl_turn_player[
                    'text'] + " : is the winner of round " + str(mainFrame.cur_round))
                if (self.frame_turn.lbl_turn_player['text'] == str(self.player1[0]).lower().capitalize()):
                    self.player1_score += 1
                    self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
                else:
                    self.player2_score += 1
                    self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
                mainFrame.cur_round += 1
                if (mainFrame.cur_round <= self.no_of_rounds):
                    self.show_frames()

        return check_val

    def do_monitor(self, x, y):
        if(x == 1):
            mainFrame.row1+=1
            mainFrame.col1+=1
            mainFrame.diag1+=1
            mainFrame.row1data.append(y)
            mainFrame.col1data.append(y)
            mainFrame.diag1data.append(y)
        elif(x == 2):
            mainFrame.row1+=1
            mainFrame.col2+=1
            mainFrame.row1data.append(y)
            mainFrame.col2data.append(y)
        elif(x == 3):
            mainFrame.row1+=1
            mainFrame.col3+=1
            mainFrame.diag2 += 1
            mainFrame.row1data.append(y)
            mainFrame.col3data.append(y)
            mainFrame.diag2data.append(y)
        elif (x == 4):
            mainFrame.row2 += 1
            mainFrame.col1+=1
            mainFrame.row2data.append(y)
            mainFrame.col1data.append(y)
        elif (x == 5):
            mainFrame.row2 += 1
            mainFrame.col2+=1
            mainFrame.diag1 += 1
            mainFrame.diag2 += 1
            mainFrame.row2data.append(y)
            mainFrame.col2data.append(y)
            mainFrame.diag1data.append(y)
            mainFrame.diag2data.append(y)
        elif (x == 6):
            mainFrame.row2 += 1
            mainFrame.col3+=1
            mainFrame.row2data.append(y)
            mainFrame.col3data.append(y)
        elif (x == 7):
            mainFrame.row3 += 1
            mainFrame.col1+=1
            mainFrame.diag2 += 1
            mainFrame.row3data.append(y)
            mainFrame.col1data.append(y)
            mainFrame.diag2data.append(y)
        elif (x == 8):
            mainFrame.row3 += 1
            mainFrame.col2+=1
            mainFrame.row3data.append(y)
            mainFrame.col2data.append(y)
        elif (x == 9):
            mainFrame.row3 += 1
            mainFrame.col3+=1
            mainFrame.diag1 += 1
            mainFrame.row3data.append(y)
            mainFrame.col3data.append(y)
            mainFrame.diag1data.append(y)

        check_result=self.do_all_check()
        if(self.no_of_btn>=9 and check_result!=1):
            self.player1_score+=1
            self.player2_score+=1
            self.side_frame.lbl_score1['text'] = "Score : " + str(self.player1_score)
            self.side_frame.lbl_score2['text'] = "Score : " + str(self.player2_score)
            tkinter.messagebox.showinfo("Winner", "Match drawn in round : "+ str(mainFrame.cur_round))
            mainFrame.cur_round += 1
            if (mainFrame.cur_round <= self.no_of_rounds):
                self.show_frames()

        if(mainFrame.cur_round>self.no_of_rounds):
            if (self.player1_score > self.player2_score):
                tkinter.messagebox.showinfo("Result", "Player 1 : " + self.player1[0] + " won")
            elif (self.player1_score > self.player2_score):
                tkinter.messagebox.showinfo("Result", "Player 1 : " + self.player2[0] + " won")
            else:
                tkinter.messagebox.showinfo("Result", "Match drawn")
            self.master.destroy()

    def switch_rbuttons(self):
        if(self.var_chk.get()==1):
            self.var_chk.set(0)
        else:
            self.var_chk.set(1)

    def do_action1(self, wname):
        if(self.var_chk.get()==1):
            self.btn1.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn1.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn1, 1))
        self.no_of_btn+=1
        self.do_monitor(1, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action2(self, wname):
        if(self.var_chk.get()==1):
            self.btn2.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn2.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn2, 2))
        self.no_of_btn += 1
        self.do_monitor(2, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action3(self, wname):
        if(self.var_chk.get()==1):
            self.btn3.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn3.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn3, 3))
        self.no_of_btn += 1
        self.do_monitor(3, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action4(self, wname):
        if(self.var_chk.get()==1):
            self.btn4.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn4.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn4, 4))
        self.no_of_btn += 1
        self.do_monitor(4, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action5(self, wname):
        if(self.var_chk.get()==1):
            self.btn5.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn5.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn5, 5))
        self.no_of_btn += 1
        self.do_monitor(5, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action6(self, wname):
        if(self.var_chk.get()==1):
            self.btn6.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn6.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn6, 6))
        self.no_of_btn += 1
        self.do_monitor(6, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action7(self, wname):
        if(self.var_chk.get()==1):
            self.btn7.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn7.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn7, 7))
        self.no_of_btn += 1
        self.do_monitor(7, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action8(self, wname):
        if(self.var_chk.get()==1):
            self.btn8.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn8.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn8, 8))
        self.no_of_btn += 1
        self.do_monitor(8, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def do_action9(self, wname):
        if(self.var_chk.get()==1):
            self.btn9.config(text='X', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        else:
            self.btn9.config(text='O', font='Times 10', fg='#4A4A4A', bg='#D0D0D0')
        mainFrame.event_log.append((self.btn9, 9))
        self.no_of_btn += 1
        self.do_monitor(9, self.var_chk.get())
        try:
            self.switch_turn()
        except Exception:
            pass
        self.switch_rbuttons()

    def show_frames(self):
        self.game_frame.destroy()
        mainFrame.row2 = 0
        mainFrame.row3 = 0
        mainFrame.col1 = 0
        mainFrame.col2 = 0
        mainFrame.col3 = 0
        mainFrame.row1 = 0
        mainFrame.diag1 = 0
        mainFrame.diag2 = 0
        self.no_of_btn=0
        mainFrame.row1data = []
        mainFrame.row2data = []
        mainFrame.row3data = []
        mainFrame.col1data = []
        mainFrame.col2data = []
        mainFrame.col3data = []
        mainFrame.diag1data = []
        mainFrame.diag2data = []
        self.game_frame = Frame(self)
        self.game_frame.pack(side='left')
        self.frame_turn = Frame(self.game_frame)
        self.frame_turn.grid(row=0, column=0, pady=6)
        self.frame_turn.lbl_turn = Label(self.frame_turn, text='Turn :', font='arial 10 bold', bg='#E5E5E5')
        self.frame_turn.lbl_turn.grid(row=0, column=0, padx=5, pady=3)
        self.frame_turn.lbl_round = Label(self.frame_turn, text="Round :" + str(mainFrame.cur_round), font='arial 10 bold', bg='#E5E5E5')
        self.frame_turn.lbl_round.grid(row=0, column=2, padx=12)
        self.frame_turn.lbl_turn_player = Label(self.frame_turn, text=str(self.player1[0]).lower().capitalize(),
                                                font='arial 10')
        self.frame_turn.lbl_turn_player.grid(row=0, column=1, padx=5, pady=3)
        self.container_frame = Frame(self.game_frame)
        self.container_frame.grid(row=1, column=0, pady=8, padx=15)
        self.container_frame.config(borderwidth=13, relief='groove')
        self.btn1 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn1.bind("<Button-1>", self.do_action1)
        self.btn1.grid(row=0, column=0, padx=2, pady=2)
        self.btn2 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn2.bind("<Button-1>", self.do_action2)
        self.btn2.grid(row=0, column=1, pady=2)
        self.btn3 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn3.bind("<Button-1>", self.do_action3)
        self.btn3.grid(row=0, column=2, padx=2, pady=2)
        self.btn4 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn4.bind("<Button-1>", self.do_action4)
        self.btn4.grid(row=1, column=0, padx=2, pady=2)
        self.btn5 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn5.bind("<Button-1>", self.do_action5)
        self.btn5.grid(row=1, column=1, pady=2)
        self.btn6 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn6.bind("<Button-1>", self.do_action6)
        self.btn6.grid(row=1, column=2, padx=2, pady=2)
        self.btn7 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn7.bind("<Button-1>", self.do_action7)
        self.btn7.grid(row=2, column=0, padx=2, pady=2)
        self.btn8 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn8.bind("<Button-1>", self.do_action8)
        self.btn8.grid(row=2, column=1, pady=2)
        self.btn9 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn9.bind("<Button-1>", self.do_action9)
        self.btn9.grid(row=2, column=2, padx=2, pady=2)

        self.bottom_frame = Frame(self.game_frame, bg='#E5E5E5')
        self.bottom_frame.grid(row=2, column=0, pady=10)
        self.var_chk = IntVar()
        self.chk1 = tkinter.ttk.Radiobutton(self.bottom_frame, text='X', padding=(4, 1), variable=self.var_chk, value=1)
        self.chk1.grid(row=0, column=0, padx=80, pady=2)
        self.chk2 = tkinter.ttk.Radiobutton(self.bottom_frame, text='O', padding=(4, 1), variable=self.var_chk, value=0)
        self.chk2.grid(row=0, column=2, padx=80, pady=2)
        self.var_chk.set(1)

    def createWidget(self):

        self.game_frame=Frame(self, bg='#ABABAB')
        self.game_frame.pack(side='left')
        self.player_frame = Frame(self)
        self.player_frame.pack(side='right')
        self.frame_turn=Frame(self.game_frame, bg='#E5E5E5')
        self.frame_turn.grid(row=0, column=0, pady=6)
        self.frame_turn.lbl_turn=Label(self.frame_turn, text='Turn :', font='arial 10 bold', bg='#E5E5E5')
        self.frame_turn.lbl_turn.grid(row=0, column=0, padx=5, pady=3)
        self.frame_turn.lbl_turn_player = Label(self.frame_turn, text=str(self.player1[0]).lower().capitalize(), font='arial 10')
        self.frame_turn.lbl_turn_player.grid(row=0, column=1, padx=5, pady=3)
        self.frame_turn.lbl_round=Label(self.frame_turn, text="Round :"+str(mainFrame.cur_round), font='arial 10 bold', bg='#E5E5E5')
        self.frame_turn.lbl_round.grid(row=0, column=2, padx=12)
        self.container_frame=Frame(self.game_frame)
        self.container_frame.grid(row=1, column=0, pady=8, padx=15)
        self.container_frame.config(borderwidth=13, relief='groove')
        self.btn1=Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn1.bind("<Button-1>", self.do_action1)
        self.btn1.grid(row=0, column=0, padx=2, pady=2)
        self.btn2 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn2.bind("<Button-1>", self.do_action2)
        self.btn2.grid(row=0, column=1, pady=2)
        self.btn3 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn3.bind("<Button-1>", self.do_action3)
        self.btn3.grid(row=0, column=2, padx=2, pady=2)
        self.btn4 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn4.bind("<Button-1>", self.do_action4)
        self.btn4.grid(row=1, column=0, padx=2, pady=2)
        self.btn5 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn5.bind("<Button-1>", self.do_action5)
        self.btn5.grid(row=1, column=1, pady=2)
        self.btn6 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn6.bind("<Button-1>", self.do_action6)
        self.btn6.grid(row=1, column=2, padx=2, pady=2)
        self.btn7 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn7.bind("<Button-1>", self.do_action7)
        self.btn7.grid(row=2, column=0, padx=2, pady=2)
        self.btn8 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn8.bind("<Button-1>", self.do_action8)
        self.btn8.grid(row=2, column=1, pady=2)
        self.btn9 = Button(self.container_frame, height=7, width=15, bd=1, relief='raised', bg='#666666')
        self.btn9.bind("<Button-1>", self.do_action9)
        self.btn9.grid(row=2, column=2, padx=2, pady=2)

        self.bottom_frame = Frame(self.game_frame, bg='#E5E5E5')
        self.bottom_frame.grid(row=2, column=0, pady=10)
        self.var_chk = IntVar()
        self.chk1 = tkinter.ttk.Radiobutton(self.bottom_frame, text='X', padding=(4, 1), variable=self.var_chk, value=1)
        self.chk1.grid(row=0, column=0, padx=80, pady=2)
        self.chk2 = tkinter.ttk.Radiobutton(self.bottom_frame, text='O', padding=(4, 1), variable=self.var_chk, value=0)
        self.chk2.grid(row=0, column=2, padx=80, pady=2)
        self.var_chk.set(1)
        self.side_frame=Frame(self.player_frame, bg='#BDBDBD')
        self.side_frame.grid(row=0, column=0, padx=5)
        self.side_frame.frame1=LabelFrame(self.side_frame, text="Player 1", fg='grey', font='arial 8 bold')
        self.side_frame.frame1.grid(row=0, column=0, padx=14, pady=45)
        self.side_frame.frame2 = LabelFrame(self.side_frame, text="Player 2", fg='grey', font='arial 8 bold')
        self.side_frame.frame2.grid(row=1, column=0, padx=14, pady=45)
        self.side_frame.lbl_name1=Label(self.side_frame.frame1, text="Player 1 :  "+str(self.player1[0]).lower().capitalize(), font='arial 8 bold')
        self.side_frame.lbl_name1.grid(row=0, column=0, pady=15, padx=4)
        self.side_frame.lbl_score1=Label(self.side_frame.frame1, text="Score :  ", font='arial 8 bold')
        self.side_frame.lbl_score1.grid(row=1, column=0, pady=15)
        self.side_frame.lbl_name2 = Label(self.side_frame.frame2, text="Player 2 :  " + str(self.player2[0]).lower().capitalize(), font='arial 8 bold')
        self.side_frame.lbl_name2.grid(row=0, column=0, pady=15, padx=4)
        self.side_frame.lbl_score2 = Label(self.side_frame.frame2, text="Score :  ", font='arial 8 bold')
        self.side_frame.lbl_score2.grid(row=1, column=0, pady=15)



root=Tk()
loginFrame(root)
root.mainloop()