import tkinter
import tkinter.messagebox
import random

class my_gui:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x500')
        self.main_window.title("Online Order")


        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        self.address = tkinter.Label(self.top_frame,text='Address: ')
        self.address_entry = tkinter.Entry(self.top_frame,width=25)

        self.address.pack(side='left')
        self.address_entry(side='left')

        