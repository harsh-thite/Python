#Lists

marks = [34, 55, 42, 13]
print(marks[0])
print(len(marks))

student = [18, "Harsh", "Delhi"]
print(student)
student[1] = "Sakshi"
print(student)   #Lists are mutable

# List Slicing
marks = [56 ,96, 45, 23, 47, 94]
print(marks[2:5])  

# Tuples
tup = (1, 2, 3, 4)
print(tup)
print(type(tup))


#Example 1
movies = ["m", "a", "a", "m"]
copy_movies = movies.copy()
copy_movies.reverse()
if(copy_movies == movies):
    print("It is palindrome")
else:
    print("It is not palindrome")  #This will always print "It is not palindrome"


#Example 2
tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))


