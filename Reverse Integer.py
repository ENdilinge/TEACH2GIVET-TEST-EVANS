#Question 5: Reverse Integer
def reverse_integer(num):
    reversed_str = str(num)[::-1]
    reversed_num = int(reversed_str)
    return reversed_num
input_integer = int(input("Enter an integer: "))

result = reverse_integer(input_integer)
print("Reversed integer:", result)
