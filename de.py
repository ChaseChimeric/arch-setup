import os
import sys
args = sys.argv
UNAME=args[1]
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
    print("Select Display Manager")
    print("1:\tLightDM\tFlexible DM, various gui forms")
    print("2:\tLy\tBasic TUI (terminal) DM, minimal but useful")
    dm = ""
    while not dm.isnumeric() or int(dm) < 1 or int(dm) > 2:
        print("select dm: ",end="")
        dm = input()
    match int(dm):
        case 1:
            LightDM()
        case 2:
            Ly()
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

def LightDM():
    print("1:\tdefault\tExtremely basic gtk based greeter")
    print("2:\tAether\tnicer looking, uses webkit")
    ldm = ""
    while not ldm.isnumeric() or int(ldm) < 1 or int(ldm) > 2:
        print("select greeter: ",end="")
        ldm = input()
    os.system("pacman -S lightdm")
    if(int(ldm) == 1):
        os.system(f'pacman -S lightdm-gtk-greeter')
    else:
        os.system(f'su --session-command="pacaur -S lightdm-webkit-theme-aether --noedit --noconfirm" {UNAME}')
    os.system("systemctl enable lightdm")

def Ly():
    os.system("pacman -S ly --noconfirm && cp configs/ly/config.ini /etc/ly")

def cosmic():
    print("installing COSMIC by System76...")
    os.system("pacman -S cosmic --noconfirm")
    
def xfce():
    print("installing XFCE4 from Xubuntu...")
    os.system(f'pacman -S xorg xorg-xwayland xfce4 xfce4-goodies --noconfirm')
def i3():
    print('installing i3...')
    os.system(f'pacman -S xorg i3 alacritty dmenu --noconfirm')
def sway():
    print('installing SwayFX...')
    os.system(f'su --session-command="yay -S swayfx --answerclean NotInstalled --answerdiff None" {UNAME}')
    os.system(f'pacman -S otf-firamono-nerd fuzzel foot --noconfirm')
    os.system(f'su --session-command="cp configs/sway/ -r /home/{UNAME}/.config/" {UNAME}')
    os.system(f'su --session-command="cp configs/waybar/ -r /home/{UNAME}/.config/" {UNAME}')
    os.system(f'su --session-command="cp configs/foot/ -r /home/{UNAME}/.config/" {UNAME}')

