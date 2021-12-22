import os
import sys


user = os.getlogin() #gets the current username


def nuke():
	os.system("shred -n 5 -v -f -z -u /home/{}/.zsh_history".format(user))
	os.system("shred -n 5 -v -f -z -u /home/{}/.bash_history".format(user))
	path = "/var/log/"
	os.system("cd {}".format(path))
	files = os.popen("ls {}".format(path)).read()
	file = files.split('\n')[:-1]
	for i in file:
		os.system("shred -n 5 -v -f -z -u {}{}".format(path, i))



def custom():
	os.system("shred -n 5 -v -f -z -u /home/{}/.zsh_history".format(user))
	os.system("shred -n 5 -v -f -z -u /home/{}/.bash_history".format(user))
	print("\n[ ? ] Enter custom path")
	path = input("\nn0trail> ")
	print("")
	files = os.popen("ls {}".format(path)).read()
	file = files.split('\n')[:-1]
	for i in file:
		os.system("shred -n 5 -v -f -z -u {}{}".format(path, i))



print("""
  ___  _             _ _ 
 / _ \| |_ _ __ __ _(_) |
| | | | __| '__/ _` | | |
| |_| | |_| | | (_| | | |
 \___/ \__|_|  \__,_|_|_|
                                                                            
""")
print("")
print("By @tensh1hx | https://github.com/tensh1hx | You can modify or redistribute the script.")
print("")

print("Welcome, what do you want to do ?")
print("")
print("[ 1 ] Erase all my logs + terminal history (doesn't support the entire directory tree)")
print("[ 2 ] I want to specify a custom path (by default /var/log/) + erase terminal history")
print("")

choice = input("n0trail> ")

choice = str(choice)

if choice == "1":
	print("[ ! ] Are you sure you want to permanently delete all of your logs? Y/n")
	warn = input("\nn0trail> ")
	print("")
	if warn == "Y":
		pass
	if warn == "n":
		print("[ * ] Goodbye")
		sys.exit()
	nuke()
	print("\n[ ... ] 50000 people used to live here. Now... it's a ghost town.")
	print("\n[ * ] Finished!")
if choice == "2":
	custom()
	print("\n[ * ] Finished!")

