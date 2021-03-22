from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    window = Tk()
    window.wm_iconbitmap("download.ico")
    window.title("Untiled - Notes_App")
    window.geometry("700x400")
    TextArea = Text(window, font=("Courier Prime", 15))
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
        self.FileMenu.add_command(label="New", command=self.newFile)
        self.FileMenu.add_command(label="Open", command=self.openFile)
        self.FileMenu.add_command(label="Save", command=self.saveFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(
            label="Exit", activebackground="red",
            command=self.quitApplication
        )
        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)

        self.EditMenu.add_command(
            label="Select All    ( Ctrl + A )", command=self.selectAll)
        self.EditMenu.add_command(
            label="Cut              ( Ctrl + X )", command=self.cut)
        self.EditMenu.add_command(
            label="Copy           ( Ctrl + O )", command=self.copy)
        self.EditMenu.add_command(
            label="Paste           ( Ctrl + V )", command=self.paste)
        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)

        self.HelpMenu.add_command(
            label="About Notepad", command=self.showAbout)
        self.MenuBar.add_cascade(label="Help", menu=self.HelpMenu)

        self.window.config(menu=self.MenuBar)
        self.Scrollbar.pack(side=RIGHT, fil=Y)

        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)

    def quitApplication(self):
        self.window.destroy()

    def showAbout(self):
        showinfo("Notepad", "This is Notepad App Created By Muhammed Savad")

    def openFile(self):
        self.file = askopenfilename(
            defaultextension=".txt", filetypes=[
                ("All Files", "'*'"),
                ("text document", "*.txt")
            ]
        )
        if self.file == "":
            self.file = None
        else:
            self.window.title(os.path.basename(self.file) + " - Notepad ")
            self.TextArea.delete(1.0, END)
            file = open(self.file, "r")
            self.TextArea.insert(1.0, file.read())
            file.close()

    def newFile(self):
        self.window.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                ("All Files", "'*'"),
                ("text document", "*.txt")
            ])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

                self.window.title(os.path.basename(self.file) + " - Notepad")

        else:
            file = open(self.file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def selectAll(self):
        self.TextArea.event_generate("<<SelectAll>>")

    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def runApp(self):
        self.window.mainloop()


notesApp = Notepad()
notesApp.runApp()
