from school_module1 import EntekhabVahed,VahedPrint

vahedha = VahedPrint("name","id","vahed","teacher")

for i in range(2):
    klass_name = input("Course name : ")
    klass_id = input("Course ID (5 digits): ")
    vahed = int(input("Units (1-7): "))
    teacher = input("Teacher name: ")

    course = EntekhabVahed(klass_name, klass_id, vahed, teacher)
    
    try:
        if course.is_valid():
            vahedha.add_klass(course)
            print("Course added successfully.")
    except Exception as e:
        print(f"Error: {e}")
print(" ")
print("--------------------------------------------------")
print("Your courses for this semester are:")
print("--------------------------------------------------")
vahedha.chap_vahed_print()
