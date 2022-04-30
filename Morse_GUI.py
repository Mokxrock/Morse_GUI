# Morse GUI
from tkinter import * # Import functions from tkinter
import tkinter.font # import fonts
from gpiozero import LED # import function from specific roles just like GPIO
import RPi.GPIO as GPIO
import time

#LED Function
red = LED(18)

# tkinter Settings
win = Tk() # Window set as Tk() 
win.title("MORSE CODE LED") # Title Of the Window
win.geometry('500x500')
myFont = (tkinter.font.Font(family = 'Helvetica', size=15, weight="bold" ))


GPIO.setmode(GPIO.BCM)
# Event Functions

# Long Blink of 1.5 seconds 
def longBlink():
    red.on()
    time.sleep(1.5)
    red.off()
    time.sleep(0.25)
    
# Short Blink of 0.25 seconds 
def shortBlink():
    red.on()
    time.sleep(0.25)
    red.off()
    time.sleep(0.25)
 # A pause or delay between each letter 
def breakBetween():
    red.off()
    time.sleep(2)

# Blink LED in Morse Code for all the letters
def morsecode(letter):
    if(letter == "a" or letter == "A"): # ._
        shortBlink()
        longBlink()
    elif (letter == "b" or letter == "B"): # _...
        longBlink()
        shortBlink()
        shortBlink()
        shortBlink()
    elif (letter == "c" or letter == "C"): # _._.
        longBlink()
        shortBlink()
        longBlink()
        shortBlink()
    elif (letter == "d" or letter == "D"): # _..
        longBlink()
        shortBlink()
        shortBlink()
    elif (letter == "e" or letter == "E"): # .
        shortBlink()
    elif (letter == "f" or letter == "F"): # .._.
        shortBlink()
        shortBlink()
        longBlink()
        shortBlink()
    elif (letter == "g" or letter == "G"): # _ _.
        longBlink()
        longBlink()
        shortBlink()
    elif (letter == "h" or letter == "H"): # ....
        shortBlink()
        shortBlink()
        shortBlink()
        shortBlink()
    elif (letter == "i" or letter == "I"): # ..
        shortBlink()
        shortBlink()
    elif (letter == "j" or letter == "J"): # ._ _ _
        shortBlink()
        longBlink()
        longBlink()
        longBlink()
    elif (letter == "k" or letter == "K"): # _._
        longBlink()
        shortBlink()
        longBlink()
    elif (letter == "l" or letter == "L"): # ._..
        shortBlink()
        longBlink()
        shortBlink()
        shortBlink()
    elif (letter == "m" or letter == "M"): # _ _
        longBlink()
        longBlink()
    elif (letter == "n" or letter == "N"): # _.
        longBlink()
        shortBlink()
    elif (letter == "o" or letter == "O"): # _ _ _
        longBlink()
        longBlink()
        longBlink()
    elif (letter == "p" or letter == "P"): # ._ _.
        shortBlink()
        longBlink()
        longBlink()
        shortBlink()  
    elif (letter == "q" or letter == "Q"): # _ _._
        longBlink()
        longBlink()
        shortBlink()
        longBlink()
    elif (letter == "r" or letter == "R"): # ._.
        shortBlink()
        longBlink()
        shortBlink()
    elif (letter == "s" or letter == "S"): # ...
        shortBlink()
        shortBlink()
        shortBlink()
    elif (letter == "t" or letter == "T"): # _
        longBlink()
    elif (letter == "u" or letter == "U"): # .._
        shortBlink()
        shortBlink()
        longBlink()
    elif (letter == "v" or letter == "V"): # ..._
        shortBlink()
        shortBlink()
        shortBlink()       
        longBlink()
    elif (letter == "w" or letter == "W"): # ._ _
        shortBlink()
        longBlink()
        longBlink()        
    elif (letter == "x" or letter == "X"): # _.._
        longBlink()       
        shortBlink()
        shortBlink()
        longBlink()
    elif (letter == "y" or letter == "Y"): # _._ _
        longBlink()       
        shortBlink()
        longBlink()
        longBlink()        
    elif (letter == "z" or letter == "Z"): # _ _..
        longBlink()       
        longBlink()
        shortBlink()
        shortBlink()        
    else: # Prompt Message of Input it's not a alphabet letter 
        lbl.config(text = " Invalid input detected ")  
 # Check the inputs and Blink name in MorseCode
def blinkLED():
    inputs = inputtxt.get( );
    if (len(inputs) <= 12): # Check if input contain maximum of 12 characters or less
        lbl.config(font=myFont, text = "Input: " + inputs + "   Length: " + str(len(inputs)))
        x=0  
        while True: # Loop Each letter 
            if(x < len(inputs) ):
                morsecode(inputs[x]) # Apply morsecode function into the index of each inputs
                x=x+1
    else:
        lbl.config(text = "Error Detected: Maximum 12 Characters or Less") # Error message if input contain more then 12 characters
            
# Textbox for entering a name  
inputtxt = Entry(win, width = 50); # Design of input box 
inputtxt.pack()
# Button TO Blink start Blinking the LED
blinkButton = Button(win, font=myFont, text= "Blink Time", command = blinkLED, bg= 'red', height = 1, width=10) 
blinkButton.pack()
lbl = Label(win, text="")
lbl.pack()
                      

win.mainloop() #Loop forever
