Name = "Suresh Kumar"
Age = "50"
first_char = Name[0]
sur_name = Name[7:]
print(Name , first_char , sur_name )
num_list = "0123456789"
print(num_list[:] , num_list[1:5] , num_list[0:4:2] , num_list[9:5:-1] , num_list[::-1])
print(Name.lower() , Name.upper() , Name.title())
print(Name.strip() , Name.replace("Kumar","Yadav") , Name.split(" ") , Name.join(" "))
print(Name.find("Kumar") , Name.count("a") , len(Name) , "Kumar" in Name)
print("My Name is {} and Age is {}".format(Name,Age))
Path = r"c:/user/pwd" # for raw string
print(Path)