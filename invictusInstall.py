"""
INvictus S3t Up
Dev: Surgat

                                                     @#@@@@@@@#@
                                                &@@,@           @,@@&
                                             @@.                     ,@@
                                           @&                           @@
                                         %@
                                        &@
                                        @
                                       &@
                @@@@@@                 &@
            .@@*      @@&              &@
          *@             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         /@                            &@
         &@                            &@
         .@                            &@
           @&           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
             #@@%,   @@@               &@
                  @@@@                 &@
                                       &@
                                       &@                                     %@@
                                       &@                  @@                    @*
                                       &@                 @. @*                  #@
                                       &@               ,@.   @#                .@,
                                       &@@@@@@@@@@@@@@@/@@@@@@@@&@@@@@@@@@@@@@@@@#
                                                      #@        @@
                                                     @@          &@
                                                    @@            (@
                                                    @%@@@@@@@@@@@@@@@
"""
import os
import sys
import signal
import subprocess
import time

#Katolin in 
def Kattool():
    print("Katoolin Installing")
    os.system('sudo apt install wget -y')
    os.system('sudo apt install gcc -y')
    os.system('sudo apt install make -y')
    os.system('wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz')
    os.system('sudo tar xzf Python-2.7.9.tgz')
    time.sleep(5)
    os.system('sudo ./Python-2.7.9/configure --enable-optimizations')
    os.system('sudo make altinstall')
    os.system('sudo ls | grep -v invictusInstall.py |xargs rm -rf')
    os.system('git clone https://github.com/LionSec/katoolin.git')
    time.sleep(5)
    os.system('sudo chmod +x katoolin/katoolin.py')
    os.system('python2.7 katoolin/katoolin.py')
    os.system('rm -rf katoolin')
    
# Apt installs 
def AptStuff():  
    print("Apt installing Tools")
    os.system('sudo apt update -y')
    os.system('sudo apt install -y nc')
    os.system('sudo apt install -y vim')
    os.system('sudo apt install -y ssh')
    os.system('sudo apt install -y telnet')
    os.system('sudo apt install -y gpsd')
    os.system('sudo apt install -y hydra')
    os.system('sudo apt install -y nikto')
    os.system('sudo apt install -y medusa')
    os.system('sudo apt install -y nmap')
    os.system('sudo apt install -y wireshark')
    os.system('sudo apt install -y tcpdump')
    os.system('sudo apt install -y hexdump')
    os.system('sudo apt install -y aircrack-ng')
    os.system('sudo apt install -y crunch')
    os.system('sudo apt install -y kismet')
    os.system('sudo apt install -y macchanger')
    os.system('sudo apt install -y wifite')
    os.system('sudo apt install -y proxychains')
    os.system('sudo apt install -y gpsd')
    os.system('sudo apt install -y dirbuster')
    os.system('sudo apt install -y cherrytree')
    
# Installer for Dr@w
def Draw():
    print("Installing Draw.io")
    os.system('wget https://github.com/jgraph/drawio-desktop/releases/download/v13.0.3/draw.io-amd64-13.0.3.deb')
    os.system('sudo dpkg -i draw.io-amd64-13.0.3.deb')
    os.system('sudo rm -rf draw.io-amd64-13.0.3.deb')

#install Meta$plo1t
def MetaBoit():
    print("MetaSploit Install")    
    os.system('sudo wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run')
    os.system('sudo chmod +x ./metasploit-latest-linux-x64-installer.run')
    os.system('sudo ./metasploit-latest-linux-x64-installer.run')
    os.system('sudo rm -rf metasploit-latest-linux-x64-installer.run')
    
#install Google Earth
def GE():
    print("Google Earth Install")
    os.system('sudo wget https://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb')
    os.system('sudo dpkg -i google-earth-stable*.deb')
    os.system('sudo rm -rf google-earth-stable*.deb')
#grub image
def gruby():
    os.system('sudo echo GRUB_BACKGROUND=/home/blacksheep/Pictures/invictusgrub.png >> /etc/default/grub')
    os.system('sudo update-grub')
    
def main():
    os.system('sudo apt update -y')
    os.system('sudo apt install -y git')
    Kattool()
    AptStuff()
    Draw()
    GE()
    MetaBoit()
    gruby()
    os.system('sudo rm -rf invictusInstall.py')
    
if __name__ == '__main__':
    main()
