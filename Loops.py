# WHILE Loops

i = 1
while i <= 5:
    print("Hey", i)
    i += 1
print(i)

# From 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop ended")


# Example 1
i = 1
while i <= 100:
    print(i)
    i += 1

# Example 2
n = int(input("Enter number:"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# Example 3
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# Example 4
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number:"))

i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Number found at Index", i)
        break
    else:
        print("finding..")
    i += 1


# FOR Loops
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter number:"))
idx = 0

for el in nums:
    if(el == x):
        print("found at index", idx)
    idx += 1
else:
    print("END")


#Ques 1
n = int(input("Enter number:"))
sum = 0
for i in range(1, n+1):
    sum += i
print("Total sum =", sum) 

#Ques 2
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact) 