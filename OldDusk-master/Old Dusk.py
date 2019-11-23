#OldDusk Version 4
#Help I dont know why any of my code doesnt work so here is a complete rewrite
import os           #Allows file opperations
import linecache    #Allows quick reading
dev = 1             #Set to 1 to have dev stuff
log = "Opened Engine Intialising (Line 6)"
Root = os.getcwd()
def StartUp():
    global log
    global Room
    log = log +"\nRunning startup function (Line 9)"
    Room = "MainMenu"
    log = log + "\nIntialised Room as " + Room
    TXT()

def TXT():
    global log
    global Root
    global Room
    log = log + "\nFunction TXT started"
    Text = open(Root +"\\data\\" + Room +"\\main.txt", "r")
    Overwrite = Text.read()
    print(Overwrite)
    Text.close()
    log =log + "\nText printed and File read completed file close (Line 26)"
    OPT()

def OPT():
    global log
    global Room
    global Select
    log = log + "\n Function OPT started"
    O01 = linecache.getline(Root + "\\data\\" + Room +"\\options.txt", 1)
    O02 = linecache.getline(Root + "\\data\\" + Room +"\\options.txt", 2)
    O03 = linecache.getline(Root + "\\data\\" + Room +"\\options.txt", 3)
    O04 = linecache.getline(Root + "\\data\\" + Room +"\\options.txt", 4)
    O05 = linecache.getline(Root + "\\data\\" + Room +"\\options.txt", 5)    
    log = log + "\n got O01-05 \n\n" + O01 + O02 + O03 + O04 + O05
    print("Options: " +O01+O02+O03+O04+O05)
    E01 = O01.upper()
    E02 = O02.upper()
    E03 = O03.upper()
    E04 = O04.upper()
    E05 = O05.upper()
    E01 = O01.upper().strip()
    E02 = O02.upper().strip()
    E03 = O03.upper().strip()
    E04 = O04.upper().strip()
    E05 = O05.upper().strip()
    log = log + "\nConverted to uppercase " + E01 + E02 + E03 + E04 + E05 + "\nStarting to prepare links"
    L01 = linecache.getline(Root + "\\data\\" + Room +"\\links.txt", 1)
    L02 = linecache.getline(Root + "\\data\\" + Room +"\\links.txt", 2)
    L03 = linecache.getline(Root + "\\data\\" + Room +"\\links.txt", 3)
    L04 = linecache.getline(Root + "\\data\\" + Room +"\\links.txt", 4)
    L05 = linecache.getline(Root + "\\data\\" + Room +"\\links.txt", 5)
    log = log + "\nLinks aquired = " +L01+L02+L03+L04+L05 + "(Line 50)"
    Select = input()
    Select = Select.upper()
    log = log + "\n Player input gained and converted to caps.\nSelect = " + Select
    print("\n")
    print(type(E01))
    print(E01)
    if Select == E01:
        Room = L01
    elif Select == E02:
        Room = L02
    elif Select == E03:
        Room = L03
    elif Select == E04:
        Room = L04
    elif Select == E05:
        Room = L05
    elif Select == "BREAK":
        print(log)
    else:
        print("Invalid Command")

    Room = Room.strip()
    TXT()
    
StartUp()   
Select = input("Oh no!\nOldDusk has encountered an error or the room doesn't exist.\nWould you like see the log? (Y/N)")
if Select == "Y":
    print(log + "End of log.\n\n\n\n Press enter to close.")
    input()
