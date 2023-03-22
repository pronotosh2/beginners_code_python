                              #Class05-2:00pm-16-03-2023-Thursday-City_IT_Park-Khalishpur.py
    #Yesterday, we discussed        if statements, lists, casting, operators, and else statements.
    #In computer programming, a loop is a sequence of instruction s that is continually repeated until a certain condition is reached.

    #there are two loops    They are 1.  for loop   and 2.  while loop 

# for loop


for i in range(10):
    print(i)                                
                                                                             # 0
                                                                             # 1
                                                                             # 2
                                                                             # 3
                                                                             # 4
                                                                             # 5
                                                                             # 6
                                                                             # 7
                                                                             # 8
                                                                             # 9
print("__________________________________________________________") # ignore this line 

for nayon in range(10):
    print(nayon)
                                                                             # 0
                                                                             # 1
                                                                             # 2
                                                                             # 3
                                                                             # 4
                                                                             # 5
                                                                             # 6
                                                                             # 7
                                                                             # 8
                                                                             # 9
print()                                                    #ignore this line 

for nayon in range(1,10):
    print(nayon)
                                                                             # 1
                                                                             # 2
                                                                             # 3
                                                                             # 4
                                                                             # 5
                                                                             # 6
                                                                             # 7
                                                                             # 8
                                                                             # 9

a=0 
for nayon in range(1,10+1):                              #range is only for number or int
    a+=10                                               # a=a+1
print(a)                                        #100

  # for loop stops after satisfying condition ,              here for is keyword 

a="akash"
for i in a:
    print(i)
                                             # a
                                             # k
                                             # a
                                             # s
                                             # h

for i in range(1,11):
    print("farzana")
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana
                                              # farzana

for i in range(1,11):
    print(i)
                                                                    # 1
                                                                    # 2
                                                                    # 3
                                                                    # 4
                                                                    # 5
                                                                    # 6
                                                                    # 7
                                                                    # 8
                                                                    # 9
                                                                    # 10

for i in range(1,11):
    print(i*2)
                                                                       # 2
                                                                       # 4
                                                                       # 6
                                                                       # 8
                                                                       # 10
                                                                       # 12
                                                                       # 14
                                                                       # 16
                                                                       # 18
                                                                       # 20

for i in range(1,11):
    print("2 X ",i," = ",i*2 )
                                                                      # 2 X  1  =  2
                                                                      # 2 X  2  =  4
                                                                      # 2 X  3  =  6
                                                                      # 2 X  4  =  8
                                                                      # 2 X  5  =  10
                                                                      # 2 X  6  =  12
                                                                      # 2 X  7  =  14
                                                                      # 2 X  8  =  16
                                                                      # 2 X  9  =  18
                                                                      # 2 X  10  =  20

                                   #Python String format() Method                   For more: https://www.w3schools.com/python/ref_string_format.asp 
                                   #The placeholder is defined using curly brackets: {}

a=5
for i in range(1,11):
    print(a,"X",i,"=",a*i)
                                    # 5 X 1 = 5
                                    # 5 X 2 = 10
                                    # 5 X 3 = 15
                                    # 5 X 4 = 20
                                    # 5 X 5 = 25
                                    # 5 X 6 = 30
                                    # 5 X 7 = 35
                                    # 5 X 8 = 40
                                    # 5 X 9 = 45
                                    # 5 X 10 = 50

                #alternative
a=5
for i in range(1,11):
    print(f"{a}X{i}={a*i}")
                                         # 5X1=5
                                         # 5X2=10
                                         # 5X3=15
                                         # 5X4=20
                                         # 5X5=25
                                         # 5X6=30
                                         # 5X7=35
                                         # 5X8=40
                                         # 5X9=45
                                         # 5X10=50

a=5
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
                                         # 5 X 1 = 5
                                         # 5 X 2 = 10
                                         # 5 X 3 = 15
                                         # 5 X 4 = 20
                                         # 5 X 5 = 25
                                         # 5 X 6 = 30
                                         # 5 X 7 = 35
                                         # 5 X 8 = 40
                                         # 5 X 9 = 45
                                         # 5 X 10 = 50


# Question: Print numbers 1 to 100. But if any number is divided by 3 instead of number, there will be print Fizz; if any number is divided by 5 instead of number, there will be print Buzz; and if any number is divided by both 3 and 5 instead of number, there will be print FizzBuzz.

for i in range(1,101):
    if i%3==0 and i%5==0:                           #indentation and used Modulus(%) instead of Division(/); ==(Equal) is Comparison operators 
        print("FizzBuzz")                           #indentation and it can not be written as print(""FizzBuzz"")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)


                                        # 1
                                        # 2
                                        # Fizz
                                        # 4
                                        # Buzz
                                        # Fizz
                                        # 7
                                        # 8
                                        # Fizz
                                        # Buzz
                                        # 11
                                        # Fizz
                                        # 13
                                        # 14
                                        # FizzBuzz
                                        # 16
                                        # 17
                                        # Fizz
                                        # 19
                                        # Buzz
                                        # Fizz
                                        # 22
                                        # 23
                                        # Fizz
                                        # Buzz
                                        # 26
                                        # Fizz
                                        # 28
                                        # 29
                                        # FizzBuzz
                                        # 31
                                        # 32
                                        # Fizz
                                        # 34
                                        # Buzz
                                        # Fizz
                                        # 37
                                        # 38
                                        # Fizz
                                        # Buzz
                                        # 41
                                        # Fizz
                                        # 43
                                        # 44
                                        # FizzBuzz
                                        # 46
                                        # 47
                                        # Fizz
                                        # 49
                                        # Buzz
                                        # Fizz
                                        # 52
                                        # 53
                                        # Fizz
                                        # Buzz
                                        # 56
                                        # Fizz
                                        # 58
                                        # 59
                                        # FizzBuzz
                                        # 61
                                        # 62
                                        # Fizz
                                        # 64
                                        # Buzz
                                        # Fizz
                                        # 67
                                        # 68
                                        # Fizz
                                        # Buzz
                                        # 71
                                        # Fizz
                                        # 73
                                        # 74
                                        # FizzBuzz
                                        # 76
                                        # 77
                                        # Fizz
                                        # 79
                                        # Buzz
                                        # Fizz
                                        # 82
                                        # 83
                                        # Fizz
                                        # Buzz
                                        # 86
                                        # Fizz
                                        # 88
                                        # 89
                                        # FizzBuzz
                                        # 91
                                        # 92
                                        # Fizz
                                        # 94
                                        # Buzz
                                        # Fizz
                                        # 97
                                        # 98
                                        # Fizz
                                        # Buzz

                
                #Polymorphism 
                # In programming, polymorphism means the same function name (but different signatures) being used for different types. In Python, polymorphisms refer to the occurrence of something in multiple forms. 

                #Every program uses else if but python uses elif
                #some programming event --> kick start 2021,codejam winner list, google code jam etceteras.
                
                    #HW:
                    #country=["Bangladesh","SriLanka","Pakistan", "Uganda","Japan"]
                    #friend=["Habib","Akash","Milon","Nayon","Nasif"]
                    #Declare king is country's first letter and name's last letter match but if doesn't declare commoner.
                    #array can stay without variable     ["","",""."",""]
                   #                                   [1,2,3,4]
                
# Re

a=["Akash","Nadia","Mim","Aysha","Sadiya","Farjana","Saikat","Mou","Tonnye","Mony","Moupia","Kaniz"]
print(a)
a.insert(2,"Dim")
print(a)
                #['Akash', 'Nadia', 'Mim', 'Aysha', 'Sadiya', 'Farjana', 'Saikat', 'Mou', 'Tonnye', 'Mony', 'Moupia', 'Kaniz']
                #['Akash', 'Nadia', 'Dim', 'Mim', 'Aysha', 'Sadiya', 'Farjana', 'Saikat', 'Mou', 'Tonnye', 'Mony', 'Moupia', 'Kaniz']
                


a=["Akash","Nadia","Mim","Aysha","Sadiya","Farjana","Saikat","Mou","Tonnye","Mony","Moupia","Kaniz"]
a.insert(2,"Dim")                                                                                                       #['Akash', 'Nadia', 'Dim', 'Mim', 'Aysha', 'Sadiya', 'Farjana', 'Saikat', 'Mou', 'Tonnye', 'Mony', 'Moupia', 'Kaniz'] 
a.remove("Mim")                                                                                                         #['Akash', 'Nadia', 'Dim', 'Aysha', 'Sadiya', 'Farjana', 'Saikat', 'Mou', 'Tonnye', 'Mony', 'Moupia', 'Kaniz'] 
a.append("Swan")                                                                                                        
print(a)

                        #['Akash', 'Nadia', 'Dim', 'Aysha', 'Sadiya', 'Farjana', 'Saikat', 'Mou', 'Tonnye', 'Mony', 'Moupia', 'Kaniz', 'Swan'] 



a=["a","b","c","d"]
a.insert(3,"cat")                       #inserting in 3 no index        #['a', 'b', 'c', 'cat', 'd']        
a.remove("c")                                                           #['a', 'b', 'cat', 'd']
print(a)

                                        #['a', 'b', 'cat', 'd']


a=["1","2","3","4"]
a.append("mango")                             
a.insert(4,"egg")                       
print(a)                
                                        #['1', '2', '3', '4', 'egg', 'mango']


a.remove("2")
print(a)



                                        #['1', '3', '4', 'egg', 'mango']



















#Extra 





# print("Enter Marks Obtained in Bangla,English,Mathematics,Physics and Chemistry")
# Bangla = float(input("Marks Obtained in Bangla:        "))
# English = float(input("Marks Obtained in English:       "))
# Mathematics = float(input("Marks Obtained in Mathematics :  "))
# Physics = float(input("Marks Obtained in Physics :      "))
# Chemistry = float(input("Marks Obtained in Chemistry :    "))
# print()

# Total = Bangla+English+Mathematics+Physics+Chemistry
# AVG = Total/5

# if AVG>=80 and AVG<=100:
#     print("A+")
# elif AVG>=70 and AVG<=79.99:
#     print("A")
# elif AVG>=60 and AVG<=69.99:
#     print("A-")
# elif AVG>=50 and AVG<=59.99:
#     print("B")
# elif AVG>=40 and AVG<=49.99:
#     print("C")
# elif AVG>=33 and AVG<=39.99:
#     print("D")
# elif AVG>=0 and AVG<=32.99:
#     print("F")
# else:
#     print("Invalid Input")








                         #For any question about this class , Our instructor:01990 709752 


                         #        Thanks for your patience.

