#Recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
show(5)


#Example 1
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
    
sum = calc_sum(5)
print(sum)

#Example 2
def print_list(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "orange"]

print_list(fruits)