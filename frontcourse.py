# Fix this file
from tkinter import *
import tkinter.messagebox
import main
import backcourse


class Course:

    def __init__(self, root):
        self.root = root
        self.root.title("UniCourse Database Management System")
        self.root.geometry("1270x740+0+0")
        self.root.config(bg="light cyan2")

        id = IntVar()
        name = StringVar()
        topic = StringVar()
        syllabus = StringVar()
        price = DoubleVar()
        description = StringVar()

        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("UniCourse Database Management Systems", "Confirm if you want to return")
            if iExit > 0:
                # backcourse.con.close()
                root.destroy()
                return main.Window(main.Tk())

        def clearData():
            self.txtCourseID.delete(0, END)
            self.txtCourseName.delete(0, END)
            self.txtTopic.delete(0, END)
            self.txtSyllabus.delete(0, END)
            self.txtPrice.delete(0, END)
            self.txtDescription.delete(0, END)

        def addData():
            if id.get() is not None:
                backcourse.add_record(id.get(), name.get(), topic.get(), syllabus.get(), price.get(), description.get())
                courselist.delete(0, END)
                courselist.insert(END,
                                  (id.get(), name.get(), topic.get(), syllabus.get(), price.get(), description.get()))

        def DisplayData():
            courselist.delete(0, END)
            for row in backcourse.view_data():
                courselist.insert(END, row, str(""))

        def CourseRec(event):
            global sd
            searchStd = courselist.curselection()[0]
            sd = courselist.get(searchStd)

            self.txtCourseID.delete(0, END)
            self.txtCourseID.insert(END, sd[0])

            self.txtCourseName.delete(0, END)
            self.txtCourseName.insert(END, sd[1])

            self.txtTopic.delete(0, END)
            self.txtTopic.insert(END, sd[2])

            self.txtSyllabus.delete(0, END)
            self.txtSyllabus.insert(END, sd[3])

            self.txtPrice.delete(0, END)
            self.txtPrice.insert(END, sd[4])

            self.txtDescription.delete(0, END)
            self.txtDescription.insert(END, sd[5])

        def DeleteData():
            if id.get() is not None:
                backcourse.delete_record(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            courselist.delete(0, END)
            for row in backcourse.search_data(id.get(), name.get(), topic.get(), syllabus.get(), price.get(),
                                              description.get()):
                courselist.insert(END, row, str(""))

        def update():
            if id.get() is not None:
                backcourse.delete_record(sd[0])
            if id.get() is not None:
                backcourse.add_record(id.get(), name.get(), topic.get(), syllabus.get(), price.get(), description.get())
                courselist.delete(0, END)
                courselist.insert(END,
                                  (id.get(), name.get(), topic.get(), syllabus.get(), price.get(), description.get()))

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
                                   font=('times new roman', 26, 'bold'), text="Course Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('times new roman', 20, 'bold'), text="Course Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # -------------------------------- Entries -------------------------------------------------- #

        self.lblCourseID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="ID:", padx=2, pady=2,
                                 bg="Ghost White")
        self.lblCourseID.grid(row=0, column=0, sticky=W)
        self.txtCourseID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=id, width=39)
        self.txtCourseID.grid(row=0, column=1)

        self.lblCourseName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Name:", padx=2, pady=2,
                                   bg="Ghost White")
        self.lblCourseName.grid(row=1, column=0, sticky=W)
        self.txtCourseName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=name, width=39)
        self.txtCourseName.grid(row=1, column=1)

        self.lblTopic = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Topic:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblTopic.grid(row=2, column=0, sticky=W)
        self.txtTopic = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=topic, width=39)
        self.txtTopic.grid(row=2, column=1)

        self.lblSyllabus = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Syllabus:", padx=2, pady=2,
                                 bg="Ghost White")
        self.lblSyllabus.grid(row=3, column=0, sticky=W)
        self.txtSyllabus = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=syllabus, width=39)
        self.txtSyllabus.grid(row=3, column=1)

        self.lblPrice = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Price:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblPrice.grid(row=4, column=0, sticky=W)
        self.txtPrice = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=price, width=39)
        self.txtPrice.grid(row=4, column=1)

        self.lblDescription = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Description:", padx=2,
                                    pady=2,
                                    bg="Ghost White")
        self.lblDescription.grid(row=5, column=0, sticky=W)
        self.txtDescription = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=description,
                                    width=39)
        self.txtDescription.grid(row=5, column=1)

        # ------------------------- scroll bar and list box ---------------------------- #

        yscrollbar = Scrollbar(DataFrameRIGHT, orient="vertical")
        yscrollbar.grid(row=0, column=1, sticky=N + S)

        xscrollbar = Scrollbar(DataFrameRIGHT, orient="horizontal")
        xscrollbar.grid(row=1, column=0, sticky=E + W)

        courselist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),
                             xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        courselist.bind('<<ListboxSelect>>', CourseRec)
        courselist.grid(row=0, column=0, padx=8)

        yscrollbar.config(command=courselist.yview)
        xscrollbar.config(command=courselist.xview)
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
    application = Course(root)
    root.mainloop()
