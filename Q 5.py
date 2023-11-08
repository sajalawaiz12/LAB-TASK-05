def count_vowels_and_consonants(word):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    # Convert the word to lowercase
    word = word.lower()

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Test the function
word = input("Enter a word: ")

vowels, consonants = count_vowels_and_consonants(word)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)