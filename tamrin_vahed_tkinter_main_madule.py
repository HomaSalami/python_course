total_course = []

for i in range (2):
    class_name = input("Enter course name : ").title()
    course_id = input("Enter course ID : ")
    credit = int(input("Enter credits : "))
    teacher = input("Enter teacher's name : ").capitalize()

    course = {"class_name":class_name, 
              "course_id": course_id,
              "credit":credit, 
              "teacher":teacher,
    }
    
    total_course.append(course)
    print("--------------------------------")

print(total_course)

sum_credit = 0
for course in total_course:
    sum_credit += course["credit"] 



#print(format chapi)
print("course_id class_name teacher credit") 
for dars in total_course:
    print(f"""{dars["course_id"]:9}, {dars["class_name"]:10}, {dars["teacher"]:10},{dars["credit"]:<10}""")

print("--------------------------------")
#sum of credits
print(f"Total Credits : {sum_credit}")





