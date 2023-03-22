                              #Class04-2:00pm-14-03-2023-Tuesday-City_IT_Park-Khalishpur
                                                                                                                                                    #Nayon1992
        # Discussion of  Conditional function : how to apply condition and what is its relationship with operaton
        #assignment operator ( = )
       
        #now We will compare two functions to see if they are equal.  " : " is refer to end of a condition.

a=10
b=20
if a==b:
    print("Equal")                  # No output 

a=10
b=10
if a==b:
    print("Equal")                  # Equal 

a=10
b=20
if a<b:
    print("Talgas")                 #Talgas

a=10
b=20
if a>b:
    print("Talgas")                 #no output 

a=100
b=20
if a>b:
    print("Talgas")                 #Talgas                    has indentation to define scope in the code.
print("Akash")                      #Akash                     has no indentation





                        # Please skip 16 lines afterwards.
                                                                         # Indentation:
                                                                         # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
                                                                         # Other programming languages often use curly-brackets for this purpose.
                                                                         #     Example:
                                                                         #     If statement, without indentation (will raise an error):


a = 33
b = 200
if b > a:
print("b is greater than a")                                          # you will get an error      like below

                                                                        # print("b is greater than a")
                                                                        #        ^
                                                                        #IndentationError: expected an indented block




a=10
b=20
if a>b:
    print("Talgass")
else:
    print("Akash")                  #Akash


         #we should be aware of where we are putting space.           space sensitive
         #we should be aware of where we are putting case.            case sensitive

    # after else we can give space before print as much as we want but minimum space is one.
    # same rule for if 
    # In print command, we generally write in string.
    #If we need to write something in print command in quotation there are two way:
           #1.  if we want to write in single quotation the string will be in double quotation  
           #2.  if we want to write in double quotation the string will be in single quotation

   # tricks # double click the words/select + shift + "
   # this is called shorthand typing or keyboard shortcut 


me="nasif"
father="shezan"
if father=="nahian":
    print("father name is correct ")
else:
    print("father name is not correct ")            #father name is not correct

me="nasif"
father="shezan"
if father=="shezan":
    print("father name is correct ")
else:
    print("father name is not correct")                                     #father name is correct

a=30
b=10
if a>b:
    print("talgas")
else:
    print("nasif")                              #talgas

a=30
b=10
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")                #a is greater than b

a=10
b=20
c=30 
if a>b and a>c: 
    print(" a is biggest")
elif b>c and b>a:
    print(" b is biggest ")
else:
    print(" c is biggest ")                     #c is biggest

a=10
b=20
c=30
if a<b and a<c:
    print(" a is smallest")
elif b<c and b<a:
    print(" b is smallest")
else:
    print(" c is smallest")                     #a is smallest

a=["Nayon","Farjana","Shukla","Nabab","Shemul","Mim"]    
if "Akash" in a:
    print("ase")
else:
    print("nai")                                #nai

a=["Nayon","Farjana","Shukla","Nabab","Shemul","Mim"]    
if "Nayon" in a:
    print("ase")
else:
    print("nai")                                #ase

             # if nasif in a then remove
a=["nasif","shezan","akash","nayon","emon"]
if "nasif" in a:
    a.remove("nasif")
print("ase")                                    #ase
print(a)                                        #['shezan', 'akash', 'nayon', 'emon'] 

a=["ridoy","nayon","batas","nasif","shamim"]
a.remove("ridoy")
a.insert(0,"akash")
print(a)                                        #['akash', 'nayon', 'batas', 'nasif', 'shamim']

a=["ridoy","nayon","milon","nasif","shamim"]
a.remove("ridoy")
a.insert(0,"akash")
if "ridoy" in a:
    print("ridoy is in a ")
else:
    print("ridoy is not in a ")                       #ridoy is not in a


            # The next class will be about loops. 
                                                           #procedure oriented 
                                                           #object oriented 
                                                           #syntax highlighting 
                                                           #end of the class 



                       #For any question about this class , Our instructor:01990 709752 


                        #        Thanks for your patience.











