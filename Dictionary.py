#Dictionaries

info = {
    "key" : "value",
    "name" : "Harsh",
    "subjects" : ["python", "c++"],
    "topic" : (dict,),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.3
       
 }
info["name"] = "Devansh"
print(info)


# NESTED DICTIONARIES

student = {
    "name" : "Harsh",
    "subjects" : {         #Nested Dict.
        "phy" : 97,
        "chem" : 92,
        "maths" : 95
        }
}
print(student["subjects"]["chem"])
print(student.get("name"))

#Updating Dictionary
new_dict = {"name" : "Devansh", "City" : "Delhi"}
student.update(new_dict)
print(student)