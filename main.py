import random

print("hello")
def classic_password():
    u = "QWERTYUIOPASDFGHJKLZXCVBNM"

    d = "qazwsxedcrfvtgbyhnujmikol"

    s = "!@#$%^&*()_+-=`~[{]}\|;:/?.>,<"

    n = "0123456789"

    all=u+d+s+n

    l = int(input("number pls: "))

    p = "".join(random.sample(all,l))

    print("your password: ",p)
    x = False
def unlimited(x = True):
    u = "QWERTYUIOPASDFGHJKLZXCVBNM"

    d = "qazwsxedcrfvtgbyhnujmikol"

    s = "!@#$%^&*()_+-=`~[{]}\|;:/?.>,<"

    n = "0123456789"

    all=u+d+s+n

    l = int(input("number pls: "))
    while x == True:
        p = "".join(random.sample(all,l))

        print("your password: ",p)

x = True

while x == True:
    print("""    [1]classic passworld
    [2]unlimited random password
    [3]quit""")
    c = int(input("pls only number: "))
    if c == 1:
        classic_password()
    elif c == 2:
        unlimited()