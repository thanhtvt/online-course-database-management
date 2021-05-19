# Fix this file
from tkinter import *
import tkinter.messagebox
import main
import backlearner


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("UniCourse Database Management System")
        self.root.geometry("1270x740+0+0")
        self.root.config(bg="light cyan2")

        id = IntVar()
        name = StringVar()
        gender = StringVar()
        dob = StringVar()
        status = StringVar()

        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("UniCourse Database Management Systems", "Confirm if you want to return")
            if iExit > 0:
                # backlearner.con.close()
                root.destroy()
                return main.Window(main.Tk())

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtName.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtSta.delete(0, END)

        def addData():
            if id.get() is not None:
                backlearner.add_record(id.get(), name.get(), gender.get(), dob.get(), status.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (id.get(), name.get(), gender.get(), dob.get(), status.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in backlearner.view_data():
                studentlist.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[0])

            self.txtName.delete(0, END)
            self.txtName.insert(END, sd[1])

            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[2])

            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[3])

            self.txtSta.delete(0, END)
            self.txtSta.insert(END, sd[4])

        def DeleteData():
            if id.get() is not None:
                backlearner.delete_record(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in backlearner.search_data(id.get(), name.get(), gender.get(), dob.get(), status.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if id.get() is not None:
                backlearner.delete_record(sd[0])
            if id.get() is not None:
                backlearner.add_record(id.get(), name.get(), gender.get(), dob.get(), status.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (id.get(), name.get(), gender.get(), dob.get(), status.get()))

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
                                   font=('times new roman', 26, 'bold'), text="Learner Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('times new roman', 20, 'bold'), text="Learner Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # -------------------------------- Entries -------------------------------------------------- #

        self.lblStdID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="ID:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=id, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Name:", padx=2, pady=2,
                             bg="Ghost White")
        self.lblName.grid(row=1, column=0, sticky=W)
        self.txtName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=name, width=39)
        self.txtName.grid(row=1, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Gender:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblGender.grid(row=2, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=gender, width=39)
        self.txtGender.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Date of Birth:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=dob, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblSta = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Employment Status:", padx=2,
                            pady=2,
                            bg="Ghost White")
        self.lblSta.grid(row=4, column=0, sticky=W)
        self.txtSta = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=status, width=39)
        self.txtSta.grid(row=4, column=1)

        # ------------------------- scroll bar and list box ---------------------------- #

        yscrollbar = Scrollbar(DataFrameRIGHT, orient="vertical")
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        xscrollbar = Scrollbar(DataFrameRIGHT, orient="horizontal")
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),
                              xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)

        yscrollbar.config(command=studentlist.yview)
        xscrollbar.config(command=studentlist.xview)

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
    application = Student(root)
    root.mainloop()
