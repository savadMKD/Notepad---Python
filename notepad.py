from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    window = Tk()
    window.wm_iconbitmap("favicon.ico")
    window.title("Untiled - Notes_App")
    window.geometry("700x400")

    def runApp(self):
        self.window.mainloop()


notesApp = Notepad()
notesApp.runApp()
