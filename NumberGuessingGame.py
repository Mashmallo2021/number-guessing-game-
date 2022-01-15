import random

set_limit = input("set a limit to guess the number ")
if set_limit.isdigit():
    set_limit=int(set_limit)
    if set_limit<=0:
        print("enter a number above 0 ")
        quit()
else:
    print("pls enter a numd=ber ")
    quit()

guess=0
random_number=random.randint(0,set_limit)

while True:
    guess+=1
    user = input("enter guess number : ")
    if user.isdigit():
        user=int(user)
    else :
        print("enter a number ")
        continue

    if user==random_number:
        print("you guess is correct ")
        break
    elif user <= random_number:
        print("your were above that number")
    else:
        print("your were below that number")

print("you got correct guess in ", guess,"times")