#Multiplication table using loops

print("Welcome to the multiplicate table")

nums = [1,2,3,4,5,6,7,8,9,10]

ask_num = int(input("Which number do you wanna do the table: "))

for mult in nums:
    result = ask_num * mult
    print(f"{ask_num} x {mult} = {result}")

