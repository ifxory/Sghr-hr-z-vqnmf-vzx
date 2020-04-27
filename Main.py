from blessings import Terminal
import os
import time
import hashlib

wrap = Terminal()
run = True
logged = False
root = False

print(wrap.clear())

time.sleep(2)
with wrap.location(0, wrap.height):
  print(wrap.bold("Login backup inited!"))
  time.sleep(1)
  print(wrap.clear())
with wrap.location(0, wrap.height):
  print(wrap.bold("Password backup inited!"))
  time.sleep(1)
  print(wrap.clear())
  time.sleep(1)

wrap.location(0, wrap.height)

while run:
  if not logged:
    print("Welcome to the MMC net. MMC(2020) All rights reserved.")
    print("For continue enter login & password")
    username = input("Login: ")
    passwd = input("Password: ")
    if not  username == "backup" and passwd == "backup":
      run = False
    logged = True
    print("Successfully logged in.")
    print("Connecting...")
    time.sleep(1)
    print("Connected with options '--public_key %s' " % hashlib.sha256("Hello gaming!".encode()).hexdigest())
    print("[INFO] $" + wrap.bold("su") + " - use this for get super user permissions.")
    print("[INFO] $" + wrap.bold("sudo") + " - use this for execute command with root permissions.")
    print("[INFO] $" + wrap.bold("exit") + " - use this for quit program.")
  if logged:
    if not root:
      cmd = input(wrap.blue("MMCnet:/ ") + wrap.bright_green("$ "))
    else:
      cmd = input("MMCnet:/ # ")
    if cmd.split(" ")[0] == "su":
      tries = 3
      while tries > 0 and not root:
        supass = input(cmd.split(" ")[0] + ": ")
        if supass == "backup":
          root = True
        else:
          tries -= 1
          print("You enter wrong password.")
    elif cmd.split(" ")[0] == "sudo":
      if not root:
        tries = 3
        while tries > 0 and not root:
          supass = input("sudo: ")
          if supass == "backup":
            root = True
            for c_cmd in cmd.split(" ")[1:]:
              os.system(c_cmd)
          else:
            tries -= 1
            print("You enter wrong password.")
      else:
        for c_cmd in cmd.split(" ")[1:]:
          os.system(c_cmd)
    elif root and cmd.split(" ")[0] == "exit":
        task = input("Do you really want to leave root? (YES/No) ")
        if task != "No" or task != "N" or task != "n" or task != "no":
          root = False
    elif not root and cmd.split(" ")[0] == "exit" or not root and cmd.split(" ")[0] == "quit":
        quit_task = input(wrap.bold("This action will cause the program to self destruct. " + "(YES/No) "))
        if quit_task != "No":
          time_count = 3000
          print(wrap.clear())
          with wrap.location(0, 0):
            print(wrap.bold("Make a wish!"))
          for i in range(time_count, 0, -1):
            with wrap.location(0, wrap.height-2):
              min = int(str(i/1000).split(".")[0])
              mills = int(str(i/1000).split(".")[1])
              print(wrap.bold_red('Remained %d.%d seconds before destruction. ' % (min, mills)))
            time.sleep(0.01)
          with wrap.location(0, wrap.height-2):
            print(wrap.clear_eos())
          with wrap.location(0, wrap.height-2):
            print(wrap.bold_red_blink("Time's up!"))
            time.sleep(1)
          run = False
