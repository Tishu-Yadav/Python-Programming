file = open("youtube.txt","r")

try:
    file.write("Hello,How are You?")
finally:
    file.close()

with open("youtube.txt","r") as file:
    file.write("Good Morning")