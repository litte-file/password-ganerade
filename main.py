import random, os
#UPDATE NOTE:jupyter is back
shild =("______________________")

def classic_password():
    uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase_letters = "qazwsxedcrfvtgbyhnujmikol"
    special_characters = "!@#$%^&*"
    numbers = "0123456789"

    all_chars = uppercase_letters + lowercase_letters + special_characters + numbers

    length = int(input("Enter password length: "))

    password = "".join(random.sample(all_chars, length))

    print("Your password: ", password)

    accept = input("Do you accept this password? (y/n): ")

    if accept == "n" or accept == "no":
        classic_password()

    elif accept == "y" or accept == "yes":
        ne = input("If you want to write a name or email, write if, if you do not want to write it, write no: ")
        ine = input("If you want to write a name or email, write if, if you do not want to write it, write no: ")
        if ne == "n" or ne == "no":
            with open("passwords.txt", "a") as f:
                f.write(shild + "\n" +"password: "+password + "\n")
            return
        with open("passwords.txt", "a") as f:
                f.write(shild + "\n" +"name/email: "+ne+"\n"+"password: "+password + "\n")
                
def unlimited():
    uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase_letters = "qazwsxedcrfvtgbyhnujmikol"
    special_characters = "!@#$%^&*"
    numbers = "0123456789"

    all_chars = uppercase_letters + lowercase_letters + special_characters + numbers

    length = int(input("Enter password length: "))

    while True:
        password = "".join(random.sample(all_chars, length))
        print("Your password: ", password)

def read_passwords():
    with open("passwords.txt", "r") as f:
        passwords = f.read()
        print(passwords)
def save_password():
    print("""
name/email:
password:
          """)
    while True:
        name_email= input("name or email enter: ")
        password= input("password enter: ")
        print("name/email: "+name_email+"\n"+"password: "+password )
        choice = input("did you write correctly y/n: ")
        if choice == "y" or choice == "yes":
            with open("passwords.txt", "a") as f:
                    f.write(shild + "\n"+"name/email: "+name_email+"\n"+"password: "+password + "\n")
            break
        if choice == "n" or choice == "no":
            print("again")
            return
while True:
    print("""    [1] Generate classic password
    [2] save password
    [3] Read saved passwords
    [4] Quit
    [5] Update""")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        classic_password()

    elif choice == 6:
        unlimited()

    elif choice == 3:
        read_passwords()

    elif choice == 4:
        break
    elif choice == 5:
        os.system("sh update.sh")

    elif choice == 2:
        save_password()

    else:
        print("Invalid choice. Please try again.")