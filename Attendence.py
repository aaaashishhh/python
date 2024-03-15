
attendence = int(input("Enter your Attendence : "));

if(attendence<=35):
    print("Don't come college ")
elif(attendence<=65):
    print("You're Defaulter ")
elif(attendence>=75):
    print("Well Performed")
elif(attendence<0 and attendence>100):
    print("Please Enter valid input")
else:
    print("Invalid")
54
