from tkinter import *
import tkinter.ttk
from main import *
from PIL import ImageTk, Image

class home_page(Frame):

    master=''

    @staticmethod
    def make_menu(master, classobj):
        master.main_menu=Menu(master)
        classobj.master.config(menu=master.main_menu)
        file_menu=Menu(master.main_menu)
        edit_menu=Menu(master.main_menu)
        view_menu=Menu(master.main_menu)
        help_menu=Menu(master.main_menu)
        master.main_menu.add_cascade(menu=file_menu, label="File")
        master.main_menu.add_cascade(menu=edit_menu, label="Edit")
        master.main_menu.add_cascade(menu=view_menu, label="View")
        master.main_menu.add_cascade(menu=help_menu, label="Help")

    def __init__(self, master):
        home_page.master=master
        super().__init__(home_page.master)
        master.minsize(400, 300)
        self.pack()
        self.create_widgets()

    def chk_click(self):
        if(self.container_frame.var_chk_showpassword.get()==1):
            self.container_frame.ent_password["show"]=""
        else:
            self.container_frame.ent_password["show"] = "*"

    def create_widgets(self):
        home_page.make_menu(self, home_page)
        self.heading_frame=Frame(self)
        self.heading_frame.pack(pady=5)
        self.heading=Label(self.heading_frame, text="Login", font=('Times New Roman', '19', 'bold', 'italic'), fg='white', bg='grey', pady=7, padx=60)
        self.heading.pack(pady=6)
        self.container_frame=Frame(self, relief="sunken")
        self.container_frame.pack(pady=10)
        self.container_frame.lbl_userId=Label(self.container_frame, text="Enter UserId", font=('', '11'))
        self.container_frame.lbl_userId.grid(row=0, column=0, pady=16, padx=8, sticky=W)
        self.container_frame.lbl_password = Label(self.container_frame, text="Enter Password", font=('', '11'))
        self.container_frame.lbl_password.grid(row=1, column=0, pady=5, padx=8, sticky=W)
        self.container_frame.var_userId=StringVar()
        self.container_frame.var_password=StringVar()
        self.container_frame.ent_userId=tkinter.ttk.Entry(self.container_frame, width=30, textvariable=self.container_frame.var_userId)
        self.container_frame.ent_password=tkinter.ttk.Entry(self.container_frame, width=30, show="*", textvariable=self.container_frame.var_password)
        self.container_frame.ent_password.grid(row=1, column=1, pady=5, padx=8)
        self.container_frame.ent_userId.grid(row=0, column=1, pady=5, padx=8)
        self.container_frame.var_chk_showpassword=IntVar()
        self.container_frame.chk_showpassword=tkinter.ttk.Checkbutton(self.container_frame, text="Show Password", variable=self.container_frame.var_chk_showpassword, onvalue=1, offvalue=0, command=self.chk_click)
        self.container_frame.chk_showpassword.grid(columnspan=2, pady=20)

        self.container_frame.btn_login=tkinter.ttk.Button(self.container_frame, text="Login", padding=(3, 3))
        self.container_frame.btn_login.grid(columnspan=2, pady=30)


class main_page(Frame):
    queobj=''
    master=''
    def __init__(self, master):
        main_page.master=master
        super().__init__(master)
        master.minsize(400, 300)
        self.pack()
        self.create_widget()


    def chk_click(self):
        if(self.container_frame.var_chk.get()==1):
            self.container_frame.ent_que["state"]="disabled"
            self.container_frame.ent_crawl["state"]="disabled"
            self.container_frame.lbl_crawl["state"]="disabled"
            self.container_frame.lbl_que["state"]="disabled"

        else:
            self.container_frame.ent_que["state"] = "normal"
            self.container_frame.ent_crawl["state"] = "normal"
            self.container_frame.lbl_crawl["state"] = "normal"
            self.container_frame.lbl_que["state"] = "normal"

    def stop_click(self):
        self.container_frame.btn_search_url.config(state="normal", text="Resume Crawling")
        self.container_frame.btn_stop["state"]="disabled"
        lockobj=threading.Condition()






    def crawl(self):
        progress_bar=Progress_bar(Toplevel(), self.thread_crawl)

        self.container_frame.btn_search_url["state"]="disabled"
        self.container_frame.btn_stop["state"]="normal"
        PROJECT_NAME = self.container_frame.var_proj.get()
        HOMEPAGE = self.container_frame.var_ent_url.get()
        main_page.queobj = Queue()
        if (self.container_frame.var_chk.get() == 0):

            QUEUE_FILE = PROJECT_NAME + '/' + self.container_frame.var_que.get() + '.txt'
            CRAWLED_FILE = PROJECT_NAME + '/' + self.container_frame.var_crawl.get() + '.txt'
            DOMAIN_NAME = get_main_domain_name(HOMEPAGE)
            NUMBER_OF_THREADS = 10
            spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, self.container_frame.var_que.get() + '.txt',
                   self.container_frame.var_crawl.get() + '.txt')
        else:
            QUEUE_FILE = PROJECT_NAME + '/queue.txt'
            CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
            DOMAIN_NAME = get_main_domain_name(HOMEPAGE)
            NUMBER_OF_THREADS = 10
            spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, 'queue.txt', 'crawled.txt')

        def create_workers(NUMBER_OF_THREADS):
            for _ in range(NUMBER_OF_THREADS):
                t = threading.Thread(target=work)
                t.daemon = True
                t.start()

        # Do the next job in the queue
        def work():
            while True:
                url = main_page.queobj.get()
                spider.crawl_page(threading.current_thread().name, url)
                main_page.queobj.task_done()

        # Each queued link is a new job
        def create_jobs(NUMBER_OF_THREADS, QUEUE_FILE):
            for link in file_to_set(QUEUE_FILE):
                main_page.queobj.put(link)
                main_page.queobj.join()
            crawl(NUMBER_OF_THREADS, QUEUE_FILE)

        # Check if there are items in the queue, if so crawl them
        def crawl(NUMBER_OF_THREADS, QUEUE_FILE):
            queued_links = file_to_set(QUEUE_FILE)
            if len(queued_links) > 0:
                print(str(len(queued_links)) + ' links in the queue')
                create_jobs(NUMBER_OF_THREADS, QUEUE_FILE)

        create_workers(NUMBER_OF_THREADS)
        crawl(NUMBER_OF_THREADS, QUEUE_FILE)


    def create_widget(self):
        home_page.make_menu(self, main_page)
        self.container_frame=Frame(self)
        self.container_frame.pack(pady=8)

        self.container_frame.labl_url=Label(self.container_frame, text="Enter Url", font=('', '11'))
        self.container_frame.labl_url.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.container_frame.var_ent_url=StringVar()
        self.container_frame.ent_url=tkinter.ttk.Entry(self.container_frame, width=35, textvariable=self.container_frame.var_ent_url)
        self.container_frame.ent_url.grid(row=0, column=1, padx=13)
        self.container_frame.var_que=StringVar()
        self.container_frame.var_crawl=StringVar()
        self.container_frame.ent_que=tkinter.ttk.Entry(self.container_frame, width=35, textvariable=self.container_frame.var_que)
        self.container_frame.ent_crawl=tkinter.ttk.Entry(self.container_frame, width=35, textvariable=self.container_frame.var_crawl)
        self.container_frame.ent_que.grid(row=1, column=1, pady=5)
        self.container_frame.ent_crawl.grid(row=2, column=1, pady=5)
        self.container_frame.lbl_que=Label(self.container_frame, text="Enter queue file", font=('', '11'))
        self.container_frame.lbl_crawl=Label(self.container_frame, text="Enter crawl file", font=('', '11'))
        self.container_frame.lbl_que.grid(row=1, column=0, pady=7, sticky=W)
        self.container_frame.lbl_crawl.grid(row=2, column=0, pady=7, sticky=W)
        self.container_frame.btn_search_url=tkinter.ttk.Button(self.container_frame, text="Start Crawling", padding=(6, 6), command=self.btn_click)
        self.container_frame.btn_stop=tkinter.ttk.Button(self.container_frame, text="Stop Crawling", padding=(6, 6), command=self.stop_click)
        self.container_frame.var_chk=IntVar()
        self.container_frame.chk_que=tkinter.ttk.Checkbutton(self.container_frame, text="Use default", variable=self.container_frame.var_chk, onvalue=1, offvalue=0, command=self.chk_click)
        self.container_frame.lbl_proj=Label(self.container_frame, text="Enter your project name", font=('', '11'))
        self.container_frame.lbl_proj.grid(row=3, column=0)
        self.container_frame.var_proj=StringVar()
        self.container_frame.ent_proj=tkinter.ttk.Entry(self.container_frame, width=35, textvariable=self.container_frame.var_proj)
        self.container_frame.ent_proj.grid(row=3, column=1, pady=7)
        self.container_frame.chk_que.grid(columnspan=2, pady=24)
        self.container_frame.btn_search_url.grid(row=5, column=0, pady=40, sticky=W, padx=23)
        self.container_frame.btn_stop.config(state="disabled")
        self.container_frame.btn_stop.grid(row=5, column=1, pady=40, sticky=E, padx=23)



    def btn_click(self):

        self.thread_crawl=threading.Thread(target=self.crawl)
        self.thread_crawl.setDaemon(TRUE)
        self.thread_crawl.setName("crawler")
        self.thread_crawl.start()


class Progress_bar(Frame):

    def __init__(self, master, threadobj):
        super().__init__(master)
        self.threadobj=threadobj
        master.minsize(360, 120)
        master.title("progress")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.progress=tkinter.ttk.Progressbar(self, length=330)
        self.progress.pack(pady=35)
        self.progress.start(25)
        if(self.threadobj.isAlive()):
            self.progress.step()
        else:
            self.progress.stop()





root=Tk()
main_obj=main_page(root)
root.mainloop()

