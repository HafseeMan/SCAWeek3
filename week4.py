import re
# Assignment: Using conditional statements, loops and regular expression in program.

attendance = ["hafsah","boy","manal","zainab","rashida"]
#checks if any of the attendees is "boy". loops through the list.
for name in attendance:
    if(name == "boy"):
        print(name + ": SCA is for GIRLS ONLY. Access denied")
    else:
        print("Welcome " + name)

answer = input("Did you complete your assignment? y/n ")

#using loop to ask questions and print phone number of regular expression
while answer == "y":
    print("Well done!")
    answer = input("Can you explain how you did it? y/n ")
    phoneNumber= input("Enter Phone number: ")

    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(phoneNumber)
    print(mo.group() + ' NOTED.')
print("Go and read. Good bye")
