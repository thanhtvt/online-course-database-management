# Fix this file
from tkinter import *
import tkinter.messagebox
import main
import backinstructor


class Instructor:

    def __init__(self, root):
        self.root = root
        self.root.title("UniCourse Database Management System")
        self.root.geometry("1270x740+0+0")
        self.root.config(bg="light cyan2")

        insid = IntVar()
        uniid = IntVar()
        name = StringVar()
        gender = StringVar()
        dob = StringVar()
        major = StringVar()

        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("UniCourse Database Management Systems",
                                                "Confirm if you want to return")
            if iExit > 0:
                # backinstructor.con.close()
                root.destroy()
                return main.Window(main.Tk())

        def clearData():
            self.txtInsID.delete(0, END)
            self.txtUniID.delete(0, END)
            self.txtInsName.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtMajor.delete(0, END)

        def addData():
            if insid.get() is not None:
                backinstructor.add_record(insid.get(), uniid.get(), name.get(), gender.get(), dob.get(), major.get())
                inslist.delete(0, END)
                inslist.insert(END, (insid.get(), uniid.get(), name.get(), gender.get(), dob.get(), major.get()))

        def DisplayData():
            inslist.delete(0, END)
            for row in backinstructor.view_data():
                inslist.insert(END, row, str(""))

        def CourseRec(event):
            global sd
            searchStd = inslist.curselection()[0]
            sd = inslist.get(searchStd)

            self.txtInsID.delete(0, END)
            self.txtInsID.insert(END, sd[0])

            self.txtUniID.delete(0, END)
            self.txtUniID.insert(END, sd[1])

            self.txtInsName.delete(0, END)
            self.txtInsName.insert(END, sd[2])

            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[3])

            self.txtDob.delete(0, END)
            self.txtDob.insert(END, sd[4])

            self.txtMajor.delete(0, END)
            self.txtMajor.insert(END, sd[5])

        def DeleteData():
            if insid.get() is not None:
                backinstructor.delete_record(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            inslist.delete(0, END)
            for row in backinstructor.search_data(insid.get(), uniid.get(), name.get(), gender.get(), dob.get(),
                                                  major.get()):
                inslist.insert(END, row, str(""))

        def update():
            if insid.get() is not None:
                backinstructor.delete_record(sd[0])
            if insid.get() is not None:
                backinstructor.add_record(insid.get(), uniid.get(), name.get(), gender.get(), dob.get(), major.get())
                inslist.delete(0, END)
                inslist.insert(END, (insid.get(), uniid.get(), name.get(), gender.get(), dob.get(), major.get()))

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
                                   font=('times new roman', 26, 'bold'), text="Instructor Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('times new roman', 20, 'bold'), text="Instructor Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # -------------------------------- Entries -------------------------------------------------- #

        self.lblInsID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Instructor ID:", padx=2,
                              pady=2,
                              bg="Ghost White")
        self.lblInsID.grid(row=0, column=0, sticky=W)
        self.txtInsID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=insid, width=39)
        self.txtInsID.grid(row=0, column=1)

        self.lblUniID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="University ID:", padx=2,
                              pady=2,
                              bg="Ghost White")
        self.lblUniID.grid(row=1, column=0, sticky=W)
        self.txtUniID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=uniid, width=39)
        self.txtUniID.grid(row=1, column=1)

        self.lblInsName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Name:", padx=2, pady=2,
                                bg="Ghost White")
        self.lblInsName.grid(row=2, column=0, sticky=W)
        self.txtInsName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=name, width=39)
        self.txtInsName.grid(row=2, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Gender:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblGender.grid(row=3, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=gender, width=39)
        self.txtGender.grid(row=3, column=1)

        self.lblDob = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Date of Birth:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDob.grid(row=4, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=dob, width=39)
        self.txtDob.grid(row=4, column=1)

        self.lblMajor = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Major:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblMajor.grid(row=5, column=0, sticky=W)
        self.txtMajor = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=major, width=39)
        self.txtMajor.grid(row=5, column=1)

        # ------------------------- scroll bar and list box ---------------------------- #

        yscrollbar = Scrollbar(DataFrameRIGHT, orient="vertical")
        yscrollbar.grid(row=0, column=1, sticky=N + S)

        xscrollbar = Scrollbar(DataFrameRIGHT, orient="horizontal")
        xscrollbar.grid(row=1, column=0, sticky=E + W)

        inslist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),
                          xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        inslist.bind('<<ListboxSelect>>', CourseRec)
        inslist.grid(row=0, column=0, padx=8)

        yscrollbar.config(command=inslist.yview)
        xscrollbar.config(command=inslist.xview)
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

        self.btnExit = Button(ButtonFrame, text="Return", font=('times new roman', 20, 'bold'), height=1, width=10,
                              bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=6)

        DisplayData()


if __name__ == '__main__':
    root = Tk()
    application = Instructor(root)
    root.mainloop()
