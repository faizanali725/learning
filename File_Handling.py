# --------------> Practice of File Handling in Python  <---------------


# -----> In file write data


file = open("mynote.txt","w")
file.write("Hello, this is a test note.\n")
file.write("This is the second line of the note.\n")
file.close()



# ---------> In file append data


file = open("mynote.txt","a")
file.write("This is an additional line added to the note.\n")
file.close()



# ---------> In file read data


file = open("mynote.txt","r")
content = file.read()
print(content)
file.close()



# ----------> In file read data line by line


with open("mynote.txt","r") as file:
    for line in file:
        print(line.strip())



# ----------> In file read data line by line using readlines()


with open("mynote.txt","r") as file:
    lines = file.readlines()
    for i in lines:
        print(i.strip())



# ----------> In file read data line by line using readline()


with open("mynote.txt","r") as file:
    lines = file.readline()
    print(lines)


# ------------> Make New File and Write Data in it <-----------------


with open("newfile.txt","w") as file:
    file.write("This is a new file created for practice.\n")
    file.write("We are learning file handling in Python.\n")
    file.write("This is the third line of the new file.\n")
    file.close()


# ----------> new file read data & use try and except..


try:
    with open("newfile.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")