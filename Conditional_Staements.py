#If statement
age = int (input("Enter your age:"))
if(age >= 18):
    print("You are old enough to drive!")
    
    
#elif statement
light = input("Enter the colour of light:")

if(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Slow down")
elif(light == "red"):
    print("Stop")


#else statement
light = input("Enter the colour of light:")

if(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Slow down")
elif(light == "red"):
    print("Stop")
else:
    print("Colour not related to traffic lights")


# Practice Ques 1:
marks = int(input("Enter your marks:"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
elif(marks >=60 and marks < 70):
    grade = "D"
else:
    grade = "F"

print("grade of the student: ", grade)