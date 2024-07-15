#!/usr/bin/env python
import os, sys

def update_checks(args):
    if "--upgrade" in args:
        command = "sudo pacman -Syu"
    elif "--update" in args:
        command = "sudo pacman -Sy"
    else:
        print("""Available args:
--update = Check for updates
--upgrade = Check for upgrades
""")
        return

    os.system(command)
    
if __name__ == "__main__":
    update_checks(sys.argv)