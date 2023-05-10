#  Class19-02:00pm-09-05-2023-Tuesday-City_IT_Park-Khalishpur.py
 
# Avoid comment or hash tag for quick process.

# Project- 
# Digital Assistance
# _voice command
# _perform the commmand using library 

# WE need library
# They are:
# pyttsx3 (python text to speech version 3)
# webbrowser 
# wikipedia 
# pywhatkit 
# speech-recognition 
# 

# They are know as library or package 
# we will install them first and then we can use them in code. 

# For installing then we need to write: pip install library_name
#                             Example:  pip install pyttsx3 
# after this press enter and the library/module will be downloading 

# Privilege:
# _text to voice convert
# _support English language 
# _support all language through Google translator 

# We will need device access of PC as most of the device runs windows. So we will use sapi5 to access mic, speaker etcetera



# Example 

import pyttsx3
neuron=pyttsx3.init("sapi5")                # init is used to initialize sapi5 in pyttsx3 module 
neuron.say("Hello,Akash")                   # if we write to this line and run we won't see output because it will run finish the program before it can say any thing. 
neuron.runAndWait()                         # after adding this line we can hear the voice. 






