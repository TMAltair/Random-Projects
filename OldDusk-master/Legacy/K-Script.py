#K-Script Ultra (Project2) by TMAltair
#This program creates rooms for text based games.
#Todo - Nothing is structured so compiled code won't work. Fix that

import os

def RoomName():
    File = open("Compiled.txt", "a+")#Opens or creates a file called Compiled.txt in same dir
    RoomTitle = input("Enter room name: ")
    File.write("def " +RoomTitle+"():\n")
    File.close()
    Text()

def Text():
    File = open("Compiled.txt", "a+")
    Txt = input("Enter Text: ")
    if Txt == "END":
        File.write("    while A==@1@:\n")
        File.write("        Select = input(@@)\n")      #Gets user input
        File.write("        Select = Select.upper()\n") #Converts input to capitals
        File.close()
        Linking1()
    else:  
        File.write("    print(@"+Txt+"@)\n")
        File.close()
        Text()

def Linking1():
    File = open("Compiled.txt", "a+")
    LnkReq = input("Enter link requirement: ") #What the user has to put to get the result
    LnkLoc = input("Enter link location: ")  #Where the user goes
    LnkReq = LnkReq.upper() #Converts the option to caps)
    File.write("        if Select == @"+ LnkReq +"@:\n")
    File.write("           "+LnkLoc+"()\n")
    File.close()
    Linking2()

def Linking2(): #Stops lots of individual ifs in one room / function
    File = open("Compiled.txt", "a+")
    LnkReq = "aaaa"
    LnkReq = input("Enter link requirement: ") #What the user has to put to get the result
    if LnkReq == "END":
        finish()
    LnkLoc = input("Enter link location") #Where the user goes
    LnkReq = LnkReq.upper() #Converts the option to caps
    File.write("        elif == "+LnkReq+":\n")
    File.write(             LnkLoc+"()\n")
    File.close()
    Linking2()

def finish():
    Sel = input("Press enter to restart or END to close.")
    if Sel == "END":
        print("")
    else:
        RoomName()

RoomName()