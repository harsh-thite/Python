# Function Definition

def calc_sum(a, b):
    return a+b

sum = calc_sum(5, 10)
print(sum)

#Avg of 3 num
def avg(a, b, c):
    return((a+b+c)/3)
average = avg(2, 4, 6)
print(average)


#Example 1
cities = ["delhi", "Chennai", "Mumbai", "Pune"]

def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(cities)

#Example 2
n = int(input("Enter n : "))

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(n)     

#Example 3
usd = int(input("Enter USD :"))

def convertor(usd):
    inr = usd * 83
    print(usd, "USD =", inr, "INR")
    
convertor(usd)


#Example 4
num = int(input("Enter number: "))

def func(num):
    if num%2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
        
func(num)