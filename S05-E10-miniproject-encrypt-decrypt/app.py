while True:
    print("choose : \n\t1) Encrypt \n\t2) Decrypt \n\t3) Exit")
    user_choose = input("Enter Number : ")
    if user_choose == "1":
        user_pm = input("Enter your txt : ")
        encrypt_pm = ""
        for chara in user_pm:
            binary = ord(chara) * 3 + 2
            encrypt_pm += chr(binary)
        print("encrypt_pm : ", encrypt_pm)
        print("\n" + "*" * 30)
    elif user_choose == "2":
        user_pm = input("Enter your txt : ")
        decrypt_pm = ""
        for chara in user_pm:
            binary = (ord(chara) - 2) // 3
            decrypt_pm += chr(binary)
        print("decrypt_pm : ", decrypt_pm)
        print("\n" + "*" * 30)
    elif user_choose == "3":
        print("Good Bye")
        break
    else:
        print("Enter write number")
