#Sets
nums = set()
nums.add(1)
nums.add(2)
nums.add("Harsh")
nums.add((1, 2, 3))

#nums.clear()  #Empties the set
print(len(nums))



# Example 1
dict = {
    "cat" : "A small animal",
    "table" : [ "A piece of furniture", "List of facts and figures"]
}
print(dict)



# Example 2 
subjects = {"python", "java", "C++", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))



# Example 3
marks = {}

x = int(input("Enter phy :"))
marks.update({"phy" : x})

x = int(input("Enter chem :"))
marks.update({"chem" : x})

x = int(input("Enter maths :"))
marks.update({"maths" : x})

print(marks)

