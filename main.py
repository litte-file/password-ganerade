import random


u = "QWERTYUIOPASDFGHJKLZXCVBNM"

d = "qazwsxedcrfvtgbyhnujmikol"

s = "!@#$%^&*()_+-=`~[{]}\|;:/?.>,<"

n = "0123456789"

all=u+d+s+n

l = 16

p = "".join(random.sample(all,l))

print("your password: ",p)