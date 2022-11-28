import bcrypt as bc
import base64 as b64
from os import system
from sys import argv

# locks or unlocks certain files
def lock_files(will_lock, file_list=["./assets", "block.tbl", "script.py", "run.sh", "README.md"]):
    for elem in file_list:
    	elem = elem.strip("\n")
    	if will_lock:
    	    system(f"sudo chmod {'000' if elem != 'run.sh' else '555'} -R {elem} > /dev/null 2>&1")
    	    system(f"sudo chattr +i -R {elem} > /dev/null 2>&1")
    	else:
    	    system(f"sudo chattr -i -R {elem} > /dev/null 2>&1")
    	    system(f"sudo chmod 777 -R {elem} > /dev/null 2>&1")

# getting info
STATE = argv[1]
if STATE == "on":
    lock_files(False)
SALT = b64.b64decode(open("./assets/salt", "rb").read())
PASS = b64.b64decode(open("./block.tbl", "r").readline().encode("utf-8"))
BLOCK = open("./block.tbl", "r").readlines()[1:]
if STATE == "on":
    lock_files(True)

# string: checks if the password is correct
def check_password(password):
    return bc.checkpw(password.encode("utf-8"), PASS)

# string: sets new password
def set_new_password(password):
    global PASS
    # composing new password
    new_pw = b64.b64encode(bc.hashpw(password.encode("utf-8"), SALT)).decode("utf-8")
    # rewriting .tbl-file
    tbl_contents = [new_pw + "\n"] + BLOCK
    if STATE == "on":
    	lock_files(False)
    write = open("./block.tbl", "w")
    write.write("".join(tbl_contents))
    write.close()
    if STATE == "on":
    	lock_files(True)
    # updating PASS variable
    PASS = b64.b64decode(new_pw.encode("utf-8"))

def print_commands():
    print("\n[P] - Change password")
    print("[E] - Change editing permissions")
    print("[Q] - Quit")
    print("[H] or [help] - List of commands\n")

def protection_enabled(prot_on):
    global STATE
    
    # update STATE variable and state file
    if STATE == "on":
    	lock_files(False)
    STATE = "on" if prot_on else "off"
    change_prot = open("./assets/state", "w")
    change_prot.write(STATE)
    change_prot.close()
    
    lock_files(STATE == "on")
    lock_files(STATE == "on", BLOCK)

if __name__ == "__main__":
    # checking password
    if check_password(input("Enter password:\n\n> ")):
    	# password is correct
    	print("\nWelcome! Choose an action:", end="")
    	print_commands()
    	while True:
    	    # getting command
    	    command = input("> ").lower()
    	    if command == "p":
    	    	# changing password
    	    	new_password = input("\nSet a new password: ")
    	    	set_new_password(new_password)
    	    	print(f"New password set! It is: \"{new_password}\"\n")
    	    elif command == "e":
    	        # changing editing permissions
    	    	protection = True if "on" in STATE else False
    	    	print("\nCurrent state of protection:", "on" if protection else "off")
    	    	print(f"Do you want to turn it {'off' if protection else 'on'}? ([Y] for yes, anything else for no)\n")
    	    	if input("> ").lower() == "y":
    	    	    # changing permission
    	    	    protection_enabled(not protection)
    	    	    print(f"\nProtection is now {'off' if protection else 'on'}!\n")
    	    	else:
    	    	    # permission not changed
    	    	    print(f"\nNo changes were made. Protection is still {'on' if protection else 'off'}.\n")
    	    elif command == "h" or command == "help":
    	    	# help command
    	    	print_commands()
    	    elif command == "q":
    	    	# quitting
    	    	print("\nGoodbye!")
    	    	break
    	    else:
    	    	# incorrect command
    	    	print("\nIncorrect command! Type 'help' for list of commands.\n")
    else:
    	# wrong password
    	print("\nIncorrect password! Access denied.")
    # relock files, if necessary
    lock_files(STATE == "on")
