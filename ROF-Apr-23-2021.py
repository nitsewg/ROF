# To qualify, I need a screenshot of the output of this code.

import time

def ShowOutput(name, time):
    print("Hey " + name + ", Welcome to the ROF Challenge for April 23rd!\n")
    print("Current time is: " + time)
    print("Here is your clue: \n\n 01010001 01010011 01001010 01111000 01110011 01101010 00111001 00101111 01100010 01110000 00101110 \n 01101111 01101111 01110110 00101111 00101111 00111010 01100110 01100011 01100111 01100111 01110101")


name = input("Please type your name: ")
current = time.strftime("%Y-%m-%d %H:%M")
ShowOutput(name, current)