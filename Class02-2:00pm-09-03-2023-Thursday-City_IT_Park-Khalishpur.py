                                                                       #   Class02-2:00pm-09-03-2023-Thursday-City_IT_Park
                # variable declaration in python
                                                                # OOP in not included 


shemul = 20
print(shemul)

milon = "10"                                           # variable declaration
milon[0]                                               # no output
print(milon[0])                                        # TERMINAL:1                          indexing starts with 0 

akash="Monirul Islam Akash"
akash[5]
print(akash[5])                                        # u

                                                            # Python is a case sensitive language. So Akash is not akash
len(akash)                                          # keyword for length 
print(len(akash))                                   # 19 

akash="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
print(len(akash))

                                                    # 613


print(akash[-5])                                    # i                        for details https://www.geeksforgeeks.org/how-to-index-and-slice-strings-in-python/ 
                                                    # Negative Index Number      generally used for large string

                  # printing First 15  (slicing 0 to 14 , not including 15)

print(akash[0:15])                                  #It is a long es               Positive Index (0 to 14) 

                 # printing after First 9  so (slicing 10 to infinity, not including infinity )
print(akash[9:])                                    #ong established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

                 #slicing  0 to 0, not including 0                for more: https://www.youtube.com/watch?v=cPypu6RLijA&t=1s                                                                                                # string[start : end : step]

                                                                                                                                                                                                                             # start : We provide the starting index.
                                                                                                                                                                                                                             # end : We provide the end index(this is not included in substring).
                                                                                                                                                                                                                             # step : It is an optional argument that determines the increment between each index for slicing.
print(akash[0:0])                                   #
  
                    #printing slicing  0 to 1, not including 1
print(akash[0:1])                                   #I

                    #printing slicing  0 to 2, not including 2
print(akash[0:2])                                   #It
print(akash[0:3])                                   #It 
print(akash[0:4])                                   #It i
print(akash[0:5])                                   #It is

print()                                              #

                  #printing slicing  -5 to infinity, not including infinity               
print(akash[-5:])                                      #ike).
print(akash[-5:-1])                                  #ike)
print(akash[-5:-2])                                  #ike
print(akash[-5:-3])                                  #ik
print(akash[-5:-4])                                  #i
print(akash[-5:-5])                                  #

print(akash[10:15])                                   #ng es
print()                                               #
print(akash[10:len(akash)])                            #ng established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
print()       

print(akash[10:])                                       #ng established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

print()       
print()       
print()       
print()       
 
# printing after slicing -613 to -12 , not including -12           in other sense printing after excluding last 12 letters

print(akash[-613:-12])                                  # #ng established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour an


akash="ABCDEFGHIJ"
print(akash[3:])   

a=input("input: ")                                      #TERMINAL: input: akash
print("output: ",a)                                    #  akash

a=input("input: ")                                     # input: akash 
print("output:"+a)                                     #akash              there are space difference in this two 

a=input("input a: ")                                   #input a: 20
b=input("input b: ")                                   #input b: 20
print(a+b)                                             #2020
                                                       #generally input is taken as str

                                 #type conversion
                                     #int() Converts to an integer.
                                                                                #float() Converts to a float.
                                                                                #str() Converts to a string.
a=int(input("input a: "))                                  #input a: 20        
b=int(input("input b: "))                                  #input b: 20
print(a+b)                                              #40
print(type(a))                                          #<class 'int'>


print(type(True))                                       #<class 'bool'>

a="habibullah"
print(a[7:])                                            #lah
print(a[-3:])                                           #lah

                                                                      #we are seeing variable declaration
                                            
a=int(input())                                          #10
b=int(input())                                          #10
print(a+b)                                              #20
print(type(a+b))                                        #<class 'int'>


mim="Symaiya Akter Mim"
print(mim[3:])                                          #aiya Akter Mim
print(mim[:-3])                                         #Symaiya Akter
print(mim[3:-3])                                        #aiya Akter

                                             # those who have no github and stackoverflow account must open these two         details in Class01
#For any question about this class , Our instructor:01990 709752 

 
  
    
    
      # one Extra (little complicated)
print(akash[::-1])                                      #JIHGFEDCBA
print(akash[-5::-1])                                    #FEDCBA
