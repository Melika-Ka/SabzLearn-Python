import time
from os import system

while True:
    print("Enter Your Choice to start timer yes or not ?")
    user_choice = input("Enter :")
    if "y" in user_choice.lower():
        hours = int(input("Enter hours : "))
        minutes = int(input("Enter minutes : "))
        seconds = int(input("Enter seconds : "))
        times = hours * 3600 + minutes * 60 + seconds
        print("timer is starting now ...")
        time.sleep(1)
        while times >= 0:
            system("cls")
            print(times)
            times -= 1
            time.sleep(1)
    elif "n" in user_choice.lower():
        pass
    else:
        print("your choice in not correct")
