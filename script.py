import os
import re
import time
import random
import keyboard
import webbrowser 

os.system('cls') 
c = open('read.txt', encoding='utf-8')
txt = c.read()

attempts = 0
loading= "....."

while True:
    attempts+=1
    print("Password (MM/DD/YYYY): ")
    ans = input()
    for i in range(5):
        print(loading[i], sep=' ', end=' ', flush=True); 
        time.sleep(random.random()*3)
    print("\n")
    if re.search(r'\b'+ re.escape(ans) + r'\b', txt, re.MULTILINE):
        webbrowser.open("https://www.yout-ube.com/watch?v=SC4xMk98Pdc&t=22s&ab_channel=PostMaloneVEVO")
        print("You succeeded! In recognition of your excellence, I now bestowe upon you this code: 32-2-12 \nWith this, please take your choice of prize A or prize B")
        break
    else:
        counter=0
        match attempts:
            case 1:
                for i in range(150):
                    keyboard.block_key(i)
                print("That was wrong- please wait")
                for i in range(int(10/5)):
                    print(str(10-5*counter)+ " seconds remaining")
                    time.sleep(5)
                    counter+=1
                keyboard.unhook_all()
            case 2:
                for i in range(150):
                    keyboard.block_key(i)
                print("Oof that was wrong too... please wait")
                for i in range(int(20/5)):
                    print(str(20-5*counter)+ " seconds remaining")
                    time.sleep(5)
                    counter+=1
                keyboard.unhook_all()
            case _:
                for i in range(150):
                    keyboard.block_key(i)
                print("Again! You must not be trying very hard...")
                for i in range(int(30/5)):
                    print(str(30-5*counter)+ " seconds remaining")
                    time.sleep(5)
                    counter+=1
                keyboard.unhook_all()

c.close()
        
 