import random
top_num = input("Type a number: ")

if top_num.isdigit():
    top_num = int(top_num)

    if top_num <= 0:
        print("please try to type a number larger than 0")
        quit()
else:
    print("please type a number next time")
    quit()

random_num = random.randrange(0, top_num)
gussess = 0

while True:
    user_guses = input("Gusses the number: ")
    gussess += 1
    if user_guses.isdigit():
        user_guses = int(user_guses)
    else:
        print("please type a number next time.")
        continue

    if user_guses == random_num:
        print("you got it!")
        break
    elif user_guses > random_num:
        print("you were above the number")
    else:
        print("you were below")
print("you got in", gussess, 'gusses')
