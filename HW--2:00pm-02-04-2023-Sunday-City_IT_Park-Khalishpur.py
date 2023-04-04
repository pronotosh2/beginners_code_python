                                                                                        #HW--2:00pm-02-04-2023-Sunday-City_IT_Park-Khalishpur.py 
                                            # This file is under processing and needs checking for errors.
a1 = []
a2 = []
a3 = []
a4 = []
n = []

for i in range(15, 251):
    if i % 3 == 0 and i % 5 == 0 and i % 8 == 0:
        a4.append(i)
    elif i % 3 == 0:
        a1.append(i)
    elif i % 5 == 0:
        a2.append(i)
    elif i % 8 == 0:
        a3.append(i)
    else:
        n.append(i)
        
# print("a1 =", a1)
# print()
# print("a2 =", a2)
# print()
# print("a3 =", a3)
# print()
# print("a4 =", a4)
# print()
# print("n =", n)
# print( "Three friends will paint Room No.: ",a4 )


print( f"Three friends will paint {a4} no. room." )
