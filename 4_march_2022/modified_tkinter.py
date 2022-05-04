from tkinter import ttk
import tkinter as tk
LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, dml_menu, mongo_db,dml_insert,dml_delete,dml_select,dml_update):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=5, column=5, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="DBMS", font=LARGEFONT)


        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="DB operations",
                             command=lambda: controller.show_frame(dml_menu),width=25)

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Architecture_details",
                             command=lambda: controller.show_frame(mongo_db),width=25)

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class dml_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DB operations", font=LARGEFONT)

        label.grid(row=0, column=2, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="insert",
                             command=lambda: controller.show_frame(dml_insert))

        # putting the button in its place
        # by using grid
        button1.grid(row=2, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Select",
                             command=lambda: controller.show_frame(dml_select))

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=1, padx=10, pady=10)
        button3 = ttk.Button(self, text="Update",
                             command=lambda: controller.show_frame(dml_update))

        # putting the button in its place by
        # using grid
        button3.grid(row=4, column=1, padx=10, pady=10)
        button4 = ttk.Button(self, text="delete",
                             command=lambda: controller.show_frame(dml_delete))

        # putting the button in its place by
        # using grid
        button4.grid(row=5, column=1, padx=10, pady=10)
        button5 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button5.grid(row=2, column=4, padx=10, pady=10)


# third window frame page2
class mongo_db(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Architecture details", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="dml_menu",
                             command=lambda: controller.show_frame(dml_menu))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

class dml_insert(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Insert", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="dml_menu",
                             command=lambda: controller.show_frame(dml_menu))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
class dml_delete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Delete", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="dml_menu",
                             command=lambda: controller.show_frame(dml_menu))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
class dml_update(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Update", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="dml_menu",
                             command=lambda: controller.show_frame(dml_menu))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
class dml_select(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        label1 = ttk.Label(self, text="Yet to be configured !!! Stay tuned for updates")
        label1.grid(row=2, column=0, padx=10, pady=10)
        button1 = ttk.Button(self, text="dml_menu",
                             command=lambda: controller.show_frame(dml_menu))

        # putting the button in its place by
        # using grid
        button1.grid(row=6, column=4, padx=10, pady=10)



# Driver Code

app = tkinterApp()
