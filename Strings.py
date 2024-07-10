# #Strings
str1 = "This is a string."
str2 = 'SRMIST is the College'
str3 = """this is a string"""
str4 = "Hey I am harsh.\n We are learning Python."
str5 = "Hey I am harsh.\t We are learning Python."
print(str4) #Prints with new line
print(str5) #Prints with tab

#Concatenation
str1 = " Hi,"
str2 = " Harsh "
final_str = str1+str2
print(final_str)

#Length of str
len1 = "Hello"
len2 = "Harsh"
final_len = len1+len2
print(len(final_len))

#Indexing
str = "Harsh Thite"
print(str[4])


#Slicing
str = "harsh thite"
# print(str[5:11]) 
print(str[:5])
print(str[6:])

#Negative Index
str = "Apple"
print(str[-3 : -1])

#String Functions
str = "Today is Day 2 of learning python"
print(str.endswith("app"))

str = "today is Day 2 of learning python"
print(str.capitalize())

str = "Today is Day 2 of learning python"
print(str.replace("o", "a"))

str = "Today is Day 2 of learning python"
print(str.find("a"))

str = "Today is Day 2 of learning python"
print(str.count("ay"))


# Practice 1:
name = input("Enter your name:")
print("length of your name is: ", len(name))

