#Opening a file 
f = open("demo.txt", "r")
data = f.read(5)
print(data)

f.close()

#Reading a file
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
f.close()
 
#Practice 1
def check_line():
    word = "good"
    data = True
    line_no = 1
    with open("demo.txt", "r") as f:
        while data:
            data = f. readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_line()