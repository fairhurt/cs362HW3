#Command to run the code: 
#python3 tyson_fairhurst_hw1.py 


year = int(input("Enter a year: "));
if((year % 4==0 and year % 100 !=0) or (year % 400 ==0)):
    print("Leap year");
else:
    print(" Not a Leap year");
