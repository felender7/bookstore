from tkinter import *
from back_end import Database

database = Database("bookstore.db")

class Window(object):

    def __init__(self,window):

        self.window = window
        self.window.wm_title("Book Store")
        self.window.geometry("580x300")
        self.window.resizable(0, 0)


        # Initiate Labels
        lbl_title = Label(window, text="Title")
        lbl_title.grid(row=0, column=0)

        lbl_author = Label(window, text="Author")
        lbl_author.grid(row=0, column=2)

        lbl_year = Label(window, text="Year")
        lbl_year.grid(row=1, column=0)

        lbl_isbn = Label(window, text="ISBN")
        lbl_isbn.grid(row=1, column=2)

        #Initiate Text input
        self.title_text = StringVar()
        self.txt_title = Entry(window, textvariable=self.title_text ,width=21,relief=RIDGE)
        self.txt_title.grid(row=0, column=1)

        self.author_text = StringVar()
        self.txt_author = Entry(window,textvariable=self.author_text, width=21,relief=RIDGE)
        self.txt_author.grid(row=0, column=3)

        self.year_text = StringVar()
        self.txt_year = Entry(window, textvariable=self.year_text ,width=21,relief=RIDGE)
        self.txt_year.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.txt_isbn = Entry(window, textvariable=self.isbn_text,width=21,relief=RIDGE)
        self.txt_isbn.grid(row=1, column=3)

        self.list_results = Listbox(window, height=10, width = 30, activestyle="none" , borderwidth=5  ,relief=RIDGE)
        self.list_results.grid(row=2,column=0, rowspan=6,columnspan=2)

        sb_results=Scrollbar(window)
        sb_results.grid(row=2,column=2, rowspan=6)

        self.list_results.configure(yscrollcommand=sb_results.set)
        sb_results.configure(command=self.list_results.yview)

        #Bind selected row to get the list
        self.list_results.bind('<<ListboxSelect>>', self.get_selected_row)

        # Initiate Buttons
        btn_view_all = Button(window,text="View All", width=21, command=self.view_command, padx = 1, pady = 10)
        btn_view_all.grid(row=2,column=3)

        btn_search = Button(window,text="Search Entry", width=21, command=self.search_command , pady = 10)
        btn_search.grid(row=3,column=3)

        btn_add = Button(window,text="Add Entry", width=21, command=self.add_command , pady = 10)
        btn_add.grid(row=4,column=3)

        btn_update = Button(window,text="Update Selected", width=21, command=self.update_command , pady = 10)
        btn_update.grid(row=5,column=3)

        btn_delete = Button(window,text="Delete Selected", width=21, command=self.delete_command , pady = 10)
        btn_delete.grid(row=6,column=3)

        btn_close = Button(window,text="Close", width=21, command=window.destroy , pady = 10)
        btn_close.grid(row=7,column=3)

    def get_selected_row(self, event):
        try:
            index=self.list_results.curselection()[0]
            self.selected_tuple=self.list_results.get(index)
            self.txt_title.delete(0, END)
            self.txt_title.insert(END, self.selected_tuple[1])
            self.txt_author.delete(0, END)
            self.txt_author.insert(END, self.selected_tuple[2])
            self.txt_year.delete(0, END)
            self.txt_year.insert(END, self.selected_tuple[3])
            self.txt_isbn.delete(0, END)
            self.txt_isbn.insert(END, self.selected_tuple[4])
        except IndexError:
            pass
            
    def view_command(self):
        self.list_results.delete(0, END)
        for row in database.view_all():
            self.list_results.insert(END, row)

    def search_command(self):
        self.list_results.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list_results.insert(END, row)


    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list_results.delete(0,END)
        self.list_results.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])

window = Tk()
Window(window)
window.mainloop()
