#Multiplication table using while loop

print("Welcome to the multiplication table!")

#This is using for and in range

#ask_num = int(input("Which number do you wanna multiplicate: "))

#for mult in range(1,11):
#    result = ask_num * mult
#    print(f"{ask_num} x {mult} = {result}")

mult = 1
ask = int(input("Which number do you want to multiplicate: "))

while mult < 11:
    print(f"{ask} x {mult} = {ask * mult}")
    mult += 1
