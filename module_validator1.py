import re
import pickle
from datetime import datetime


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]+$",name):
        raise NameError("Try Name Again!")
    
def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$",brand):
        raise NameError("Try Brand Again!")

def quantity_validator(quantity):
    if not (quantity > 0 and type(quantity) == int):
        raise NameError("Try Quantity Again!")

def price_validator(price):
    if not (price > 0 and type(price) == int):
        raise NameError("Try Price Again!")
    
def exp_validator(exp_date):
    expire_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
    if not expire_date >= datetime.today().date():
        raise NameError ("Try EXP Date Again!")    


def save_to_file(product_list):
    shopping_file = open("shopping_list" , "wb")
    pickle.dump(product_list , shopping_file) 
    shopping_file.close()   

def total_product(product_list):
    total = 0
    for item in product_list:
        total += item["quantity"]*item["price"]
    return total

#def show_product(product_list):
    #for product in product_list:
        #pass