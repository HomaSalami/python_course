from module_validator1 import *
from tkinter import *
from tkinter import messagebox
from datetime import datetime

product_list = []

def save():
    try:
        # get every parameter from user,and check if data validation based on module file
        name_validator(name.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(price.get())
        exp_validator(exp_date.get())

        # check if data validator was +, then put in dict and add to product_list
        product = {"name": name.get(),
                   "brand":brand.get(),
                   "quantity":quantity.get(),
                   "price":price.get(),
                   "exp_date":exp_date.get()
                   }
        
        product_list.append(product)
        save_to_file(product_list)
        messagebox.showinfo("Saved!", "Product has joined the list Happily :)")
        name.set("")
    except Exception as e:
        messagebox.showerror("OoPS! Save Error!!!", f"Error: {e}")


def total():
    try:
        #todo total
        total_product(product_list)
        messagebox.showinfo("Total Price", f"Total Price is : {total_product(product_list)} TOMAN ")
    except Exception as e:
        messagebox.showinfo("Oops! Error!!!", f"Error: {e}")



window = Tk()
window.title("Shopping")
window.geometry("320x320")

#name
Label(window,text="Name").place(x=30,y=30)
name = StringVar()
Entry(window,textvariable = name).place(x=120,y=30)

#brand
Label(window,text="Brand").place(x=30,y=70)
brand = StringVar()
Entry(window,textvariable = brand).place(x=120,y=70)

#quantity
Label(window,text="Quantity").place(x=30,y=110)
quantity = IntVar()
Entry(window,textvariable=quantity).place(x=120,y=110)

#price
Label(window,text="Price").place(x=30,y=150)
price = IntVar()
Entry(window,textvariable=price).place(x=120,y=150)

#expire_date
Label(window,text="Expiration Date\n YYYY-MM-DD").place(x=30,y=190)
exp_date = StringVar()
Entry(window,textvariable=exp_date).place(x=120,y=190)


Button(window,text="Save", command=save).place(x=30,y=255,width=100)
Button(window,text="Total",command=total).place(x=145,y=255,width =100)
window.mainloop()