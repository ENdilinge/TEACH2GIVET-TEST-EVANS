#Question 3: Power of Two
def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

num = int(input("Enter an integer: "))

result = is_power_of_two(num)
print(f"{num} is a power of two: {result}")
