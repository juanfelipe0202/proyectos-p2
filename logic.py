import random
def genaradorpassword(length):
    elements = "abcdefghijklmnopqrstuvwxyzñ1234567890+-/*!&$#?=@<>"
    elements += "abcdefghijklmnopqrstuvwxyzñ1234567890+-/*!&$#?=@<>".upper()
    password = ""
    for i in range(length):
            password += random.choice(elements)

    return password
print(genaradorpassword(10))
