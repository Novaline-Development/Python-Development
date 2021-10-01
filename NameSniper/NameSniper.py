import json
import requests
import random
import string
from os import system
import threading
import multiprocessing
import signal
import re
import time
import os

class ThreadedNameGen:
    def __init__(self, chars):
        self.chars = chars
        if mode == 1 or mode == 3:
            self.letters = string.ascii_letters + string.digits + "_"
        elif mode == 2:
            self.letters = "Il"
    
    def check_acc_with_underscore(self):
        while True:
            a = ''.join(random.choice(self.letters) for _ in range(2)) + "_" + ''.join(random.choice(self.letters) for _ in range(2))
            if a.count("_") < 2:
                data = requests.get(f"https://auth.roblox.com/v1/usernames?username={a}").json()
                if a in data["usernames"]:
                    print(f"X | {a} Not Available")
                else:
                    with open("usernames.txt", "a+") as fw:
                        fw.write(a + "\n")
                    print(f"V | {a} Is Available | Name has been logged to file usernames.txt!")
    
    def check_acc(self):
        while True:
            a = ''.join(random.choice(self.letters) for _ in range(self.chars))
            if not a.count("_") > 2:
                data = requests.get(f"https://auth.roblox.com/v1/usernames?username={a}").json()
                if a in data["usernames"]:
                    print(f"X | {a} Not Available")
                else:
                    with open("usernames.txt", "a+") as fw:
                        fw.write(a + "\n")
                    print(f"V | {a} Is Available | Name has been logged to file usernames.txt!")


if __name__ == "__main__":
    system('title Novaline NameSniper')
    print(r" _   _                        _____       _                  ")
    print(r"| \ | |                      /  ___|     (_)                 ")
    print(r"|  \| | __ _ _ __ ___   ___  \ `--. _ __  _ _ __   ___ _ __  ")
    print(r"| . ` |/ _` | '_ ` _ \ / _ \  `--. \ '_ \| | '_ \ / _ \ '__| ")
    print(r"| |\  | (_| | | | | | |  __/ /\__/ / | | | | |_) |  __/ |    ")
    print(r"\_| \_/\__,_|_| |_| |_|\___| \____/|_| |_|_| .__/ \___|_|    ")
    print(r"                                           | |               ")
    print(r"                                           |_|               ")
    print("Made By SirWeeb, charliebrasso and Lunah.")
    print("SirWeeb - making the program and adding the modes")
    print("charliebrasso - requests code")
    print("Lunah - fixing up threading")
    try:
        with open('usernames.txt', 'w') as f:
            f.write("")
    except OSError:
        print("\nSomething blocked me from writing to files, was it your anti-virus?")
        input("Press any key to exit.")
        exit()
    char_amount = None
    while True:
        mode = input("1) Normal mode.\n2) Barcode mode.\n3) 5 character with underscore in the middle. \nWhich mode would you like to use? ")
        try:
            mode = int(mode)
            if mode > 3:
                print("There's only 3 modes!")
                continue
        except ValueError:
            print("The mode must be a number.")
            continue
        threads = input(f"How many cores would you like to use? You have {multiprocessing.cpu_count()} inside of your computer. ")
        try:
            threads = int(threads)
            if threads > multiprocessing.cpu_count():
                print("You don't have that many cores!")
                continue
        except ValueError:
            print("Thread amount must be a number.")
            continue
        if mode != 3:
            char_amount = input("How long does the username have to be? ")
            try:
                char_amount = int(char_amount)
            except ValueError:
                print("Character amount must be a number.")
                continue
            if char_amount < 5:
                print("All 1, 2, 3 and 4 character names are taken.")
                continue
            if char_amount > 20:
                print("20 is the maximum allowed characters.")
                continue
            if mode == 2:
                if char_amount < 15:
                    input("A character amount over 15 is recommended for sniping barcodes, however this isn't needed. (Press enter.)")
        break
    for _ in range(threads):
        gen = ThreadedNameGen(char_amount)
        if mode == 1 or mode == 2:
            proc = threading.Thread(target=gen.check_acc, args=[])
        elif mode == 3:
            proc = threading.Thread(target=gen.check_acc_with_underscore, args=[])
        proc.daemon = True
        proc.start()
    while True:
        time.sleep(1)
