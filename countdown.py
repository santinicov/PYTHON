#Countdown using for loop and while loop

print("Hi, welcome!!")

ask_num = int(input("Type how long you want to countdown: "))


"""for count in range(ask_num, 0, -1 ):
    print(count)

print("GOOOO!!")"""

while ask_num >= 1:
    print(ask_num)
    ask_num -= 1