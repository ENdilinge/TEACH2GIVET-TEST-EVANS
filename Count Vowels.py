
# Question 6: Count Vowels
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)
input_sentence = input("Enter a sentence: ")
vowel_count = count_vowels(input_sentence)
print(f"For input '{input_sentence}', the program returns '{vowel_count}'.")
