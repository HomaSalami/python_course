from tkinter import *
from tkinter import messagebox



window = Tk()
window.title("انتخاب واحد")
window.geometry("300x300")

#class_name
Label(window,text="class_name").place(x=20,y=20)
class_name = StringVar()
Entry(window,textvariable = class_name).place(x=100,y=20)

#course_id

Label(window,text="course_id").place(x=20,y=60)
course_id = StringVar()
Entry(window,textvariable = course_id).place(x=100,y=60)

#credit

Label(window,text="credit").place(x=20,y=100)
credit = IntVar()
Entry(window,textvariable=credit).place(x=100,y=100)

#teacher
Label(window,text="teacher").place(x=20,y=140)
teacher = StringVar()
Entry(window,textvariable=teacher).place(x=100,y=140)


#Button(window,text="Save", command=save).place(x=40,y=240,width=80)
#Button(window,text="Sum of Credits",command=total).place(x=150,y=240,width = 80)
window.mainloop()