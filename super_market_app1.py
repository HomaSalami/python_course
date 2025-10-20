from tkinter import *
from tkinter import messagebox
product_list = []

def save():
    try:
        # if data validation
        product = {"name": name.get(), "brand":brand.get(), "quantity":quantity.get() ,"price":price.get() ,"exp_date":exp_date.get()}
        product.append(product)
        messagebox.showinfo("Save", "Product Saved")
        name.set("")

    except Exception as e:
        pass

def total():
    try:
        pass
    except Exception as e:
        pass


window = Tk()
window.title("kharid")
window.geometry("300x300")

#name
Label(window,text="Name").place(x=20,y=20)
name = StringVar()
Entry(window,textvariable = name).place(x=100,y=20)

#brand

Label(window,text="Brand").place(x=20,y=60)
brand = StringVar()
Entry(window,textvariable = brand).place(x=100,y=60)

#quantity

Label(window,text="Quantity").place(x=20,y=100)
quantity = IntVar()
Entry(window,textvariable=quantity).place(x=100,y=100)

#price
Label(window,text="Price").place(x=20,y=140)
price = IntVar()
Entry(window,textvariable=price).place(x=100,y=140)

#expire_date
Label(window,text="Exp. Date").place(x=20,y=180)
exp_date = StringVar()
Entry(window,textvariable=exp_date).place(x=100,y=180)


Button(window,text="Save", command=save).place(x=40,y=240,width=80)
Button(window,text="Total",command=total).place(x=150,y=240,width = 80)
window.mainloop()