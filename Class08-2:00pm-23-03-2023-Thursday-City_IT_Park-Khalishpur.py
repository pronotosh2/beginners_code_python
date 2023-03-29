#Class08-2:00pm-23-03-2023-Thursday-City_IT_Park-Khalishpur.py

# Funtion recap                                  # Next library 

# Topic:
# why will we learn programming language?
 # for making task easier
 # for making new  task 
 # for removing communication gap between human and machine
 # etceteras
# python learning purpose 
 # easy to learn
 # easy to use 
 # multipurpose 
 # machine learning, AI, python cross platform kivy etceteras. 
# 
# 
# 
# why is php dying? 
# It is not multipurpose language
# It is not up-to-date 
# people are not willing to learn it 
# there are easier language. 
# 


# now-a-days , people need multitasking. 
# So a django developer(Title only) has to learn vm, react, node js, jest API etceteras for markets' demand.


# Recap:

print(20)                                   # 20
print(type(20))                             #

            #when 2 + 2 is bigger than 4
print("2"+"2")                              # 22 
                                                            # How to concat 2 strings in Python?
                                                            # Use the + operator
                                                            # The + operator can be used to concatenate two different strings.
                                                            # Python String Concatenation can be done using various ways.


                                                #Why are numbers called floats?
                                                #Floating point numbers get their name from the way the decimal point can "float" to any position necessary. 
                                                #dotted number are called float.



for i in range(1,101):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)


print()
print()
print()
print()

# Make three(perhaps four) Fizz,Buzz & FizzBuzz( and N). the numbers of Fizz will go into list Fizz,the numbers of Buzz will go into list Buzz
# and the numbers of FizzBuzz will go into list FizzBuzz.



Fizz=[]
Buzz=[]
FizzBuzz=[]
N=[]
for i in range(1,101):
    if i%3==0 and i%5==0:
        FizzBuzz.append(i)
    elif i%5==0:
        Buzz.append(i)
    elif i%3==0:
        Fizz.append(i)
    else:
        N.append(i)
print(N)
print()
print(Fizz)
print(Buzz)
print(FizzBuzz)
print()
print()
print()
print()
print("N= ",N)
print()
print("Fizz= ",Fizz)
print("Buzz= ",Buzz)
print("FizzBuzz= ",FizzBuzz)
print("======================================================================================================")



# Five's Multiplication Table
print()
print()
print()
print()
# while loop,    
# please skip 17 lines 
a=5
i=1
while True:
    if a==50:
        break
    print("5 X ",i,"=",a)
    i=i+1
    a=a+5
    


print()
print()
print()
print()
print()






                                     # Don't use this experimental 
a=0
while True:
    if a==50:
        break
    a=a+5
    print(a)


print("____________________________________________________________________________________________________")
print()
print()
print("Five's Multiplication Table")
print()
print()
print()
# Five's Multiplication Table

for i in range(1,11):
    print("5 X ",i,"=",i*5)


            
            
            # Function: function is a bunch of code which solves certain problem. 
            # Its characteristics:
            # must be defined 
            # must have a name 
            # must have parameters
            # must have body 
            # must have return  
            # like this example:  
            # def akash():
            #     return                # indention must be given wheather if is in function or not 
           

print()
print()
print()
print("____________________________________________________________________________________________________")
print()
print()
print()


def akash():
    for i in range(10):                   # alignment must be maintain, keeping a indention means we are writing under body
        pass
    if 1==2:
        pass



print()
print("def means define")
print("---------------------------------------------------------------------------------------------------")
print()
                                                 # def means define 

def akash(x,t):
    for i in range(1,101):
        if i%x==0 and i%t==0:
            print("FizzBuzz")
        elif i%t==0:
            print("Buzz")
        elif i%x==0:
            print("Fizz")
        else:
            print(i)
akash(5,9)
print()                                                                             # parameter/argument,   CSS variable
akash(5,6)
print()
akash(8,9)
print()
akash(7,9)
print()
akash(6,9)
print()

print("_________________________________________________________________________")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("------------------------------------")


def akash(x,t,a,b):
    for i in range(a,b):

        akash(5,9,1,101)
        print(akash(5,9,1,101))






