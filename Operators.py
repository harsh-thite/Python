# 1)Arithmetic Operators
a = 5
b= 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Modular_Operator
print(a%2)  # remainder
# Power_operator
print(a**b)



# 2)Relational Operators
a = 50
b = 30

print(a == b)  #false
print(a != b)  #true
print(a <= b)  #false
print(a >= b)  #true



# 3)Assignment Operators
num = 10
num += 10 #20
num -= 10
num *= 10
num **= 10
print("num :", num)



#Logical Operators
#Not_operator
a = 50 
b = 30
print(not False)
print(not (a > b))

#and_operator (Gives true only when all the values are assigned as True)
val1 = True
val2 = True
print("AND operator:", val1 and val2)

#or_operator (True if any value = True)
val1 = True
val2 = False
print("OR operator:", val1 or val2)
print("OR operator:", (a == b) or (a > b)) #(50 != 30, 50 > 30, Overall = True)
