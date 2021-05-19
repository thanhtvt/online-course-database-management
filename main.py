from tkinter import *
import tkinter.messagebox
import frontcourse
import frontlearner
import frontuni
import frontinstructor


class Window:

    def __init__(self, root):
        self.root = root
        self.root.title("UniCourse Database Management System")
        self.root.geometry("900x500+0+0")
        self.root.config(bg="light cyan2")

        # -------------------------------------- FUNCTIONS --------------------------------------- #

        def iExit():
            iExit = tkinter.messagebox.askyesno("UniCourse Database Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def call_learner():
            root.destroy()
            return frontlearner.Student(frontlearner.Tk())

        def call_course():
            root.destroy()
            return frontcourse.Course(frontcourse.Tk())

        def call_instructor():
            root.destroy()
            return frontinstructor.Instructor(frontinstructor.Tk())

        def call_uni():
            root.destroy()
            return frontuni.University(frontuni.Tk())

        MainFrame = Frame(self.root, bg="light cyan2")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=25, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame, font=('times new roman', 35, 'bold'), text="UniCourse Database Management System",
                            bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=20, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # ----------------------------------- #

        self.btnLearner = Button(ButtonFrame, text="Learner Management", font=('times new roman', 20, 'bold'), height=1,
                                 width=20,
                                 bd=4, command=call_learner)
        self.btnLearner.grid(row=0, column=0, padx=10, pady=10)

        self.btnCourse = Button(ButtonFrame, text="Course Management", font=('times new roman', 20, 'bold'), height=1,
                                width=20, bd=4, command=call_course)
        self.btnCourse.grid(row=1, column=0, padx=10, pady=10)

        self.btnInstructor = Button(ButtonFrame, text="Instructor Management", font=('times new roman', 20, 'bold'),
                                    height=1, width=20, bd=4, command=call_instructor)
        self.btnInstructor.grid(row=2, column=0, padx=10, pady=10)

        self.btnUni = Button(ButtonFrame, text="University Management", font=('times new roman', 20, 'bold'), height=1,
                             width=20, bd=4, command=call_uni)
        self.btnUni.grid(row=3, column=0, padx=10, pady=10)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExit)
        self.btnExit.grid(row=4, column=0, padx=10, pady=10)


if __name__ == '__main__':
    root = Tk()
    application = Window(root)
    root.mainloop()
