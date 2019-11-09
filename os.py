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

print "================[HidHunt]================="
print "==     Author   : Hidhunt       	=="
print "==     Wa       : 088214804205  	=="
print "==     Youtube  : Sasmita 2113  	=="
print "==     Instagram: Sasmita_2103  	=="
print "=================[~~~~~]=================="
7
print "\n\nMenu : "
print ""
print "[1] Ubuntu (rekomendasi utk pemula)"
print "[2] Debian"
print "[3] Kali"
print "[4] Kali Nethunter"
print "[5] Parrot Security"
print "[6] BackBox"
print "[7] Fedora"
print "[8] CentOS"
print "[9] OpenSUSE Leap"
print "[10] OpenSUSE Tumbleweed"
print "[11] Arch Linux"
print "[12] Black Arch"
print "[13] Alpine"
print ""
print "[00] keluar\n"
i = raw_input("HidHunt@os > ")

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
 print "[!] Error: wrong input!"
 time.sleep (1)
 res()

# Kalo error wasap gw ya
