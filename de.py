""" For later
    add gnome4
    add some kde thing
    add cinnamon?
"""
import os
import sys
import time
import random
#environ stuff
args = sys.argv
UNAME=args[1]

# install function defs
def grubtheme():
    os.system("git clone https://github.com/vinceliuice/Elegant-grub2-themes")
    os.system("Elegant-grub2-themes/install.sh")
    match random.randint(0,3):
        case 0:
            os.system("Elegant-grub2-themes/install.sh -b -t wave --type window")
        case 1:
            os.system("Elegant-grub2-themes/install.sh -b -t mojave --type window")
        case 2:
            os.system("Elegant-grub2-themes/install.sh -b -t forest --type window")
        case 3:
            os.system("Elegant-grub2-themes/install.sh -b -t mountain --type window")
    os.system("rm -r Elegant-grub2-themes")
def LightDM():
    # ldm has 2 options for the greeter, but base install is simple through pacman
    print("1:\tdefault\tExtremely basic gtk based greeter")
    print("2:\tAether\tNicer looking, uses webkit")
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
    text = ""
    output = ""
    with open("/etc/lightdm/lightdm.conf", 'r') as inputfile:
        text = inputfile.readlines()
    for line in text:
        if "#greeter-session=" in line:
            output += "greeter-session=lightdm-webkit2-greeter\n"
        else:
            output += line
    with open("/etc/lightdm/lightdm.conf", 'w') as outputfile:
        outputfile.write(output)

def Ly():
    # nice and easy
    os.system("pacman -S ly --noconfirm && cp configs/ly/config.ini /etc/ly")
    if(random.randint(0,10) == 0):
        os.system("mv /etc/ly/config.ini.copy /etc/ly/config.ini")
    os.system("systemctl enable ly")

def cosmic():
    # simple group install
    print("\x1b[38;5;214minstalling COSMIC by System76...\x1b[0m")
    time.sleep(2)
    os.system("pacman -S cosmic --noconfirm")
    
def xfce():
    # also pretty easy, doesn't install xorg for some reason
    print("\x1b[38;5;214minstalling XFCE4 from Xubuntu...\x1b[0m")
    time.sleep(2)
    os.system(f'pacman -S xorg xorg-xwayland xfce4 xfce4-goodies --noconfirm')
    os.system(f'su --session-command="pacaur -S iwgtk --noedit --noconfirm" {UNAME}')

def i3():
    # same here xorg isn't initially required for some reason, also installs basic stuff to run programs
    print('\x1b[38;5;214minstalling i3...\x1b[0m')
    time.sleep(2)
    os.system(f'pacman -S xorg i3 alacritty dmenu --noconfirm')
    os.system(f'su --session-command="pacaur -S iwgtk --noedit --noconfirm" {UNAME}')
def sway():
    # y this so hard, probably installs the most stuff--personal configs included
    print('\x1b[38;5;214minstalling SwayFX...\x1b[0m')
    time.sleep(2)
    os.system(f'su --session-command="yay -S swayfx --answerclean NotInstalled --answerdiff None" {UNAME}')
    os.system(f'pacman -S  fuzzel foot xorg xorg-xwayland waybar pulseaudio pulseaudio-alsa pavucontrol --noconfirm')
    os.system(f'su --session-command="cp configs/sway/ -r /home/{UNAME}/.config/" {UNAME}')
    os.system(f'su --session-command="cp configs/waybar/ -r /home/{UNAME}/.config/" {UNAME}')
    os.system(f'su --session-command="cp configs/foot/ -r /home/{UNAME}/.config/" {UNAME}')
    os.system(f'su --session-command="pacaur -S iwgtk --noedit --noconfirm" {UNAME}')




confirm = input("\x1b[38;5;214minstall Desktop Environment? (y/n) \x1b[0m")
if confirm == "y":
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
    os.system("pacman -S firefox otf-firamono-nerd --noconfirm")
    grubtheme();
    print("DE has been installed, just reboot and login")
else:
    exit()


