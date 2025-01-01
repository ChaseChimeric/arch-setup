import os
confirm = input("install Desktop Environment? (y/n) ")
if confirm:
    #prompt de
    print("1:\tCOSMIC\tgnome like, easiest")
    print("2:\txfce4\tlighter full de, also easy")
    print("3:\ti3\tstandard tiling window manager, pretty hard")
    print("4:\tSwayFX\tWayland based wm, as hard as i3") 
    de = ""
    while not de.isnumeric() or int(de) < 1 or int(de) > 4:
        print("select de: ",end="")
        de = input()
    match int(de):
        case 1:
            cosmic()
        case 2:
            xfce()
        case 3:
            i3()
        case 4:
            sway()
        case default:
            exit()
else:
    exit()

def cosmic():
    print("installing COSMIC by System76...")
    
def xfce():
    print()
def i3():
    print()
def sway():
    print()