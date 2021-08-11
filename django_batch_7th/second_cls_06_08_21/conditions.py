isVersityOpen = True
lockdown = False
# if elif else

# nested condition
if isVersityOpen == True:
    print("it is true, so i will go, but is it lockdown out of there?")
    if lockdown == True:
        print("It is possible that i going for the class")
    else:
        print("Lockdown is over, so i can go for my class")
else:
    print("it is not true.")

# if else ladder

cgpa = 3.2

if cgpa >= 3.7 and cgpa <= 4.0:
    print('A+')
elif cgpa >= 3.0 and cgpa <= 3.6:
    print('B+')
elif cgpa >=2.5  and cgpa <= 2.9:
    print('C+')
else:
    print("F")


