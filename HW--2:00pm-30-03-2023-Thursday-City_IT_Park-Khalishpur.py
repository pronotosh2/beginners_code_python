                                                                                              #HW--2:00pm-30-03-2023-Thursday-City_IT_Park-Khalishpur.py
print("Please Enter Marks Obtained in Bangla, English, Mathematics, Physics and Chemistry")
Bangla=float(input("Marks Obtained in Bangla: "))
English=float(input("Marks Obtained in English: "))
Mathematics=float(input("Marks Obtained in Mathematics: "))
Physics=float(input("Marks Obtained in Physics: "))
Chemistry=float(input("Marks Obtained in Chemistry: "))

Total=Bangla+English+Mathematics+Physics+Chemistry
AVG=Total/5
if AVG>=80 and AVG<=100:
    print("Letter Grade (LG):A+ & CGPA 4.00")
elif AVG>=75 and AVG<80:
    print("Letter Grade (LG):A & CGPA 3.75")
elif AVG>=70 and AVG<75:
    print("Letter Grade (LG):A- & CGPA 3.50")
elif AVG>=65 and AVG<70:
    print("Letter Grade (LG):B+ & CGPA 3.25")
elif AVG>=60 and AVG<65:
    print("Letter Grade (LG):B & CGPA 3.00")
elif AVG>=55 and AVG<60:
    print("Letter Grade (LG):B- & CGPA 2.75")
elif AVG>=50 and AVG<55:
    print("Letter Grade (LG):C+ & CGPA 2.50")
elif AVG>=45 and AVG<50:
    print("Letter Grade (LG):C & CGPA 2.25")
elif AVG>=40 and AVG<45:
    print("Letter Grade (LG):D & CGPA 2.00")
elif AVG>=0 and AVG<40:
    print("Letter Grade (LG):F")
else:
    print("Invalid Input")
