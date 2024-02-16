#Question 1: FizzBuzz

num = int(input("Enter a number between 1 and 100: "))

if 1 <= num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
else:
    print("Please enter a number between 1 and 100.")
