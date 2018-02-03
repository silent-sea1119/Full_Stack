dict = {"Rollno":17, "Name" : "Akshay"}
print dict

dict["Class"] = "BE-B"
print dict

##Update with user input
x = int(input("Ener Roll No : "))
y = raw_input("Ener Name : ")
z = raw_input("Ener Class : ")

dict["Rollno"] = x
dict["Name"] = y
dict["Class"] = z

print dict 
