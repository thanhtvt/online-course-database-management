# Fix this file
from tkinter import *
import tkinter.messagebox
import main
import backuni


class University:

    def __init__(self, root):
        self.root = root
        self.root.title("UniCourse Database Management System")
        self.root.geometry("1270x740+0+0")
        self.root.config(bg="light cyan2")

        id = IntVar()
        name = StringVar()
        website = StringVar()
        description = StringVar()

        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("UniCourse Database Management Systems", "Confirm if you want to return")
            if iExit > 0:
                # backuni.con.close()
                root.destroy()
                return main.Window(main.Tk())

        def clearData():
            self.txtUniID.delete(0, END)
            self.txtUniName.delete(0, END)
            self.txtWebsite.delete(0, END)
            self.txtDes.delete(0, END)

        def addData():
            if id.get() is not None:
                backuni.add_record(id.get(), name.get(), website.get(), description.get())
                unilist.delete(0, END)
                unilist.insert(END, (id.get(), name.get(), website.get(), description.get()))

        def DisplayData():
            unilist.delete(0, END)
            for row in backuni.view_data():
                unilist.insert(END, row, str(""))

        def CourseRec(event):
            global sd
            searchStd = unilist.curselection()[0]
            sd = unilist.get(searchStd)

            self.txtUniID.delete(0, END)
            self.txtUniID.insert(END, sd[0])

            self.txtUniName.delete(0, END)
            self.txtUniName.insert(END, sd[1])

            self.txtWebsite.delete(0, END)
            self.txtWebsite.insert(END, sd[2])

            self.txtDes.delete(0, END)
            self.txtDes.insert(END, sd[3])

        def DeleteData():
            if id.get() is not None:
                backuni.delete_record(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            unilist.delete(0, END)
            for row in backuni.search_data(id.get(), name.get(), website.get(), description.get()):
                unilist.insert(END, row, str(""))

        def update():
            if id.get() is not None:
                backuni.delete_record(sd[0])
            if id.get() is not None:
                backuni.add_record(id.get(), name.get(), website.get(), description.get())
                unilist.delete(0, END)
                unilist.insert(END, (id.get(), name.get(), website.get(), description.get()))

        # -------------------------------------- Frames ---------------------------------------------- #

        MainFrame = Frame(self.root, bg="light cyan2")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame, font=('times new roman', 40, 'bold'), text="UniCourse Database Management System",
                            bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame = Frame(MainFrame, bd=2, width=1250, height=70, padx=19, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1250, height=400, padx=20, pady=20, relief=RIDGE, bg="light cyan2")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('times new roman', 26, 'bold'), text="University Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('times new roman', 20, 'bold'), text="University Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # -------------------------------- Entries -------------------------------------------------- #

        self.lblUniID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="ID:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblUniID.grid(row=0, column=0, sticky=W)
        self.txtUniID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=id, width=39)
        self.txtUniID.grid(row=0, column=1)

        self.lblUniName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Name:", padx=2, pady=2,
                                bg="Ghost White")
        self.lblUniName.grid(row=1, column=0, sticky=W)
        self.txtUniName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=name, width=39)
        self.txtUniName.grid(row=1, column=1)

        self.lblWebsite = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Website:", padx=2, pady=2,
                                bg="Ghost White")
        self.lblWebsite.grid(row=2, column=0, sticky=W)
        self.txtWebsite = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=website, width=39)
        self.txtWebsite.grid(row=2, column=1)

        self.lblDes = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Description:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDes.grid(row=3, column=0, sticky=W)
        self.txtDes = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=description, width=39)
        self.txtDes.grid(row=3, column=1)

        # ------------------------- scroll bar and list box ---------------------------- #

        yscrollbar = Scrollbar(DataFrameRIGHT, orient="vertical")
        yscrollbar.grid(row=0, column=1, sticky=N + S)

        xscrollbar = Scrollbar(DataFrameRIGHT, orient="horizontal")
        xscrollbar.grid(row=1, column=0, sticky=E + W)

        unilist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),
                          xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        unilist.bind('<<ListboxSelect>>', CourseRec)
        unilist.grid(row=0, column=0, padx=8)

        yscrollbar.config(command=unilist.yview)
        xscrollbar.config(command=unilist.xview)

        # -------------------------------------- Buttons --------------------------------------- #

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10,
                                 bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1,
                                     width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10,
                                   bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Return", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=6)

        DisplayData()


if __name__ == '__main__':
    root = Tk()
    application = University(root)
    root.mainloop()
