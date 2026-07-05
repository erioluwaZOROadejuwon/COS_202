print("="*18)
print("POCKET CGPA CALCULATOR")
print("="*18)
total_course_unit=0
total_points=0
unit=0
num_courses=int(input("How many courses do you offer: "))
for i in range(num_courses):
    unit=int(input("Enter the course unit of these: "))
    grade=input("Enter your grade: ")
    if grade=="A":
        point=5
    elif grade=="B":
        point=4
    elif grade=="C":
        point=3
    elif grade=="D":
        point=2
    elif grade=="E":
        point=1
    elif grade=="F":
        point=0
    else:
        print("Invalid grade")
    total_points=total_points+(point*unit)
    total_course_unit=total_course_unit+unit
cgpa=total_points/total_course_unit
print("Your CGPA IS: ", cgpa)
if cgpa==5.00:
    print("YOU GOT A PERFECT CGPA CONGRATS")
elif cgpa>=4.5:
    print("FIRST CLASS HONOURS")
elif cgpa>=3.5:
    print("SECOND CLASS UPPER HONOURS")
elif cgpa>=2.5:
    print("SECOND CLASS LOWER HONOURS")
elif cgpa>=1.5:
    print("THIRD CLASS HONOURS")
else:
    print("WORK ON YOURSELF!!!")
