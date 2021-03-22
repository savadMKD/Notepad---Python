from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    window = Tk()
    window.wm_iconbitmap("favicon.ico")
    window.title("Untiled - Notes_App")
    window.geometry("700x400")
    TextArea = Text(window, font=("Arial", 15))
    MenuBar = Menu(window)

    FileMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)
    HelpMenu = Menu(MenuBar, tearoff=0)

    Scrollbar = Scrollbar(TextArea)
    file = None

    def __init__(self):
        # Text Area Risize
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky=N+S+E+W)

        # File Menu
        self.FileMenu.add_command(label="New")
        self.FileMenu.add_command(label="Open")
        self.FileMenu.add_command(label="Save")
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", activebackground="red")
        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)

        self.EditMenu.add_command(label="Select All    ( Ctrl + A )")
        self.EditMenu.add_command(label="Cut              ( Ctrl + X )")
        self.EditMenu.add_command(label="Copy           ( Ctrl + O )")
        self.EditMenu.add_command(label="Paste           ( Ctrl + V )")
        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)

        self.HelpMenu.add_command(label="About Notepad")
        self.MenuBar.add_cascade(label="Help", menu=self.HelpMenu)

        self.window.config(menu=self.MenuBar)
        self.Scrollbar.pack(side=RIGHT, fil=Y)

        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)

    def runApp(self):
        self.window.mainloop()


notesApp = Notepad()
notesApp.runApp()
