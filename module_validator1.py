import re

total = 0

def name_vallidator(name):
    if re.match(r"^[a-zA-Z\s]$",name):
        return True
    else:
        return False
    
def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{3,30}$",brand):
        return True
    else:
        return False


def save_to_file(product_list)
    pass

def total() 
    pass

def show_product(product_list):
    for product in product_list:
        pass