import tkinter as tk
from tkinter import filedialog
import os
import shutil
root = tk.Tk()
root.withdraw()

def Menu():
    print("Select operation:\nInstall\nHelp\nClose\n")
    Select = input("Select a operation: ")
    Select = Select.upper()
    if Select == "INSTALL":
        Install()
    elif Select == "HELP":
        print("1) Select your CastleMinerZ.exe (This will be from steam)\n2)Now select the modded CastleMinerZ.exe\n3)Select the folder where CMZ is stored")
    elif Select == "CLOSE":
        exit()
    else:
        print("Invalid command.")


def Install():
    print("Select CMZ.exe (The one from steam)")
    os.remove(filedialog.askopenfilename())
    print("Select mod then CMZ Directory (Where steam stores CMZ)")
    shutil.copy(filedialog.askopenfilename(),filedialog.askdirectory(), follow_symlinks=True)

    
Menu()
