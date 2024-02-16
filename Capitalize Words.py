#Question 4: Capitalize Words
def capitalize_words(input_string):
    words = input_string.split()

    capitalized_words = [word.capitalize() for word in words]

    
    result_string = ' '.join(capitalized_words)

    return result_string

input_string = input("Enter a string: ")

result = capitalize_words(input_string)
print("Capitalized string:", result)
