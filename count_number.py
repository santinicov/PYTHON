#This is for understanding the concept of loops in Python.

print("Hi this is a counter of numbers using loops in Python.")

number_count = 0

ask_number = int(input("From 1 to how much you want to count: "))

while number_count < ask_number:
    number_count +=1
    print(number_count)
