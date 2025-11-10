import re

class EntekhabVahed:
    def __init__(self,klass_name,klass_id,vahed,teacher):
        self.klass_name = klass_name
        self.klass_id = klass_id
        self.vahed = vahed
        self.teacher = teacher

    def is_valid(self):
        if not re.match(r"^[a-zA-Z\s\d]{3,15}$",self.klass_name):
            raise NameError("Invalid Name!")
        
        if not re.match(r"^[\d]{5}$", self.klass_id):
            raise NameError("Error! Enter the 5 digit course ID again.")

        if not (type(self.vahed) == int and 0 < self.vahed < 7):
                #todo
            raise NameError("Error! Enter a 1 digit number.")

        if not re.match(r"^[a-zA-Z\s]{3,15}$", self.teacher):
            raise NameError("Invalid Name!")

        return True   
    
class VahedPrint:
    def __init__(self, klass_name,klass_id, vahed, teacher):
        self.klass_name = klass_name
        self.klass_id = klass_id
        self.vahed = vahed
        self.teacher = teacher
        self.klass_list = []

    def add_klass(self, klass):
        self.klass_list.append(klass)

    def get_total(self):
        if not self.klass_list:
            raise ValueError("No such course available")

        total = 0
        for k in self.klass_list:
            total +=k.vahed
            #todo total += vahed
        return total

    def chap_vahed_print(self):
        print(f"{'#':3} {'ID':10} {'Title':10} {'Teacher':10} {'Credits':3}")
        num_klass = 0
        for k in self.klass_list:
            print(f"\t{num_klass}{k.klass_id:10}{k.klass_name.capitalize():11}{k.teacher.title():10}{k.vahed:3}")
            num_klass += 1
            #todo num_class namayesh dade nemishavad
        print("--------------------------------------------------")
        print("Total Courses:" , num_klass)
        print("Total Credits:" , self.get_total())
