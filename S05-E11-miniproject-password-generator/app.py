import random
import string

lower_cases = string.ascii_lowercase
upper_cases = string.ascii_uppercase
chars = "~!@#$%^&*()_+-=\|/?><"
numbers = "0123456789"
all_chars = lower_cases + upper_cases + chars + numbers
while True:
    print("Enter Your Choice : \n\t1) Password\n\t2) Exit")
    user_choice = input("Enter Your Choice Number : ")
    if user_choice == "1":
        pass_length = int(input("Enter Password Length"))
        password = "".join(random.sample(all_chars, pass_length))
        print(password)
        print("\n" + "*" * 30)
        pass
    elif user_choice == "2":
        break
    else:
        print("Enter Correct Number")
