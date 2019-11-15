#apa wooyy mau recode?
# Hargai ngapa njir, capek bikin nya nih
# Gblk, ubah author gk jadiin lu pemilik
# Mau belajar bikin script?
# Wa gw aja nih 0882-1480-4205
# Ntar bljr bareng

import os, sys, time


def res():
  python = sys.executable
  os.execl(python, python, * sys.argv)
  curdir = os.getcwd()

os.system("clear")

n='\033[0m'
redx='\033[1;31m'
hijaux='\033[1;32m'
kuningx='\033[1;33m'
birux='\033[1;34m'
ungux='\033[1;35m'
cyanx='\033[1;36m'

print hijaux+"================"+kuningx+"[HidHunt]"+hijaux+"================="
print hijaux+"==    "+cyanx+" Author   : Hidhunt       	"+hijaux+"=="
print hijaux+"==    "+cyanx+" Wa       : 088214804205  	"+hijaux+"=="
print hijaux+"==    "+cyanx+" Youtube  : Sasmita 2113  	"+hijaux+"=="
print hijaux+"==     "+cyanx+"Instagram: Sasmita_2103"+hijaux+"  	=="
print hijaux+"=================["+ungux+"~~~~~"+hijaux+"]=================="

print birux+"\n\nMenu : "
print ""
print kuningx+"[1]"+cyanx+" Ubuntu (rekomendasi utk pemula)"
print kuningx+"[2]"+ungux+" Debian"
print kuningx+"[3]"+birux+" Kali"
print kuningx+"[4]"+hijaux+" Kali Nethunter"
print kuningx+"[5]"+kuningx+" Parrot Security"
print kuningx+"[6]"+redx+" BackBox"
print kuningx+"[7]"+cyanx+" Fedora"
print kuningx+"[8]"+kuningx+" CentOS"
print kuningx+"[9]"+birux+" OpenSUSE Leap"
print kuningx+"[10]"+ungux+" OpenSUSE Tumbleweed"
print kuningx+"[11]"+hijaux+" Arch Linux"
print kuningx+"[12]"+redx+" Black Arch"
print kuningx+"[13]"+cyanx+" Alpine"
print ""
print redx+"[00]"+hijaux+" keluar\n"
i = raw_input(birux+"HidHunt@os > "+n)

if i == 1:
 print "installing ubuntu..."
 time.sleep(1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
 print ""
 print "./start-ubuntu.sh untuk start!\n"

elif i == 2:
 print "installing debian..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
 print ""
 print "./start-debian.sh untuk start!\n"

elif i == 3:
 print "installing kali..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
 print ""
 print "./start-kali.sh untuk start!\n"

elif i == 4:
 print "installing kali nethunther..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
 print ""
 print "./start-nethunter.sh untuk start!\n"

elif i == 5:
 print "installing Parrot Security os..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
 print ""
 print "./start-parrot.sh untuk start!\n"

elif i == 6:
 print "installing BackBox..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
 print ""
 print "./start-backbox.sh utuk start!\n"

elif i == 7:
 print "installing fedora..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
 print ""
 print "./start-fedora.sh untuk start!\n"

elif i == 8:
 print "installinh CentOS..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
 print ""
 print "./start-centos.sh untuk start!\n"

elif i == 9:
 print "installing openSUSE Leap..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
 print ""
 print "./start-leap.sh untuk start!\n"

elif i == 10:
 print "installing openSUSE Tumbleweed..."
 time.sleep (1)
 print ""
 print "./start-tumbleweed.sh untuk start!\n"

elif i == 11:
 print "installing Arch Linux..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")
 print ""
 print "./start-arch.sh untuk start!\n"

elif i == 13:
 print "installing Black Arch..."
 time.sleep (1)
 os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
 print ""
 print "./start-arch.sh untuk start!\n"

elif i == 13:
 print "installing Alpine..."
 time.sleep (1)
 os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
 print ""
 print "./start-alpine.sh untuk start!\n"

elif i == "00":
 os.system("exit")

else:
 print "\033[1;31m[!] Error: wrong input!"
 time.sleep (1)
 res()

# Kalo error wasap gw ya
