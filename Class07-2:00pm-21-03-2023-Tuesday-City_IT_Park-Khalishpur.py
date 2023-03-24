#Class07-2:00pm-21-03-2023-Tuesday-City_IT_Park-Khalishpur.py




# Skip / do not read the hashtag lines(comments) for quick progress. 





#Topic: Function  

    #solution

food=500                                 #known value
day=0                                    #unknown
while True:
    if food <=1:
        break
    food = food/2                        # alt food/=2
    day = day+1
print(day)
                                     # 9 
                                     # For zoom of VS Code --> Ctrl + (+ of Num)

#Topic-01-Function: function is set of programs or bunch of programs which is used to solve a certain problem. 
# How to call data from one page to another  (of course in same folder)

# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result. 

# Creating a Function
# In Python a function is defined using the def keyword:
# Example:
# def my_function():
#   print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:
# Example
# def my_function():
#   print("Hello from a function")

# my_function()







# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

                                                                                                                                                                       #"If a child can't learn the way we teach, maybe we should teach the way they learn" - Ignacio Esatrada.


# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.









# call.py

a=20
b=30
if a>b:
    print(a)
else:
    print(b)


                 

                 # Note:
                 # Dividend = Divisor x Quotient + Remainder        

                 # % will give us reminder not quotient.  
                 #  division factor:    A factor is a number that divides another number, leaving no remainder. 
                 # 




            # function's keyword def
            # def akash()                            # keyword name(argument/parameter)
            # 

def sg(a,b):            
    if a>b:
        print(a)
    else:
        print(b)

print(sg(5,15))
                                                    # 15
                                                    # None 


def sg(a,b):
    if a>b:
        print(a)
    else:
        print(b)
sg(20,30)
                                            # 30



                                                # def sg(a,b):
                                                #     if a>b:
                                                #         print(a)
                                                #     else:
                                                #         print(b)
                                                #             sg(20,30)
                                                #
                                                # IndentationError: unexpected indent




                            # from .. import *                    ..  is file name.     *     asterisk,A star-shaped figure (*) 
                            # * means all here. 
                            # 
                            # from akash import*
                            # sg(30,40)                       
                            #                                    # 40





                             #File:akash.py
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
                                                # answer is too big to write


                                  # file.py
                                  # from akash import*
                                  # print(i(i,))
                #Problem:
                #Create two file. In first file, solve problem gupi and in second file call it.





                            # File:akash.py 

def sg(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)
sg(20,50,90)


                            # file.py 
                            #from akash import*
                            #print(sg(5,10,15))
















                         #For any question about this class , Our instructor:01990 709752 


                         #        Thanks for your patience.
