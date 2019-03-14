from tkinter import *
from tkinter import filedialog
class texteditor:
    current_open_file = "no_file"
    def openfile(self):
        openreturn = filedialog.askopenfile(title="Open file", filetypes=(("text files","*.txt"),("all files","*.*")))
        if (openreturn != None):
            self.text.delete(1.0, END)
            for i in openreturn:
                self.text.insert(INSERT,i)
            self.current_open_file = openreturn.name
            openreturn.close()

    def saveasfile(self):
        savereturn = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        if savereturn is None:
            return
        savetext = self.text.get(1.0, END)
        savereturn.write(savetext)
        self.current_open_file = savereturn.name
        savereturn.close()

    def savefile(self):
        if (self.current_open_file == "no_file"):
            self.saveasfile()
        else:
            f = open(self.current_open_file,"w+")
            f.write(self.text.get(1.0, END))
            f.close()

    def newfile(self):
        self.text.delete(1.0, END)
        self.current_open_file="no_file"


    def copytext(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def cuttext(self):
        self.copytext()
        self.text.delete("sel.first","sel.last")

    def pastetext(self):
        self.text.insert(INSERT, self.text.clipboard_get())


    def __init__(self,master):
        self.master = master
        self.text = Text(self.master, undo=True)
        self.text.pack(fill=BOTH,expand=1)
        master.title("Gdext")
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        #Creating File menu
        self.filemenu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_command(label="Save as", command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit)

        #Creating Edit menu
        self.editmenu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Undo", command=self.text.edit_undo)
        self.editmenu.add_command(label="Redo",command=self.text.edit_redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.cuttext)
        self.editmenu.add_command(label="Copy", command=self.copytext)
        self.editmenu.add_command(label="Paste", command=self.pastetext)


root = Tk()
te = texteditor(root)
root.mainloop()