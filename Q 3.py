def check_anagram(word1, word2):
    # Convert both words to lowercase and remove any spaces
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Check if the lengths of the words are equal
    if len(word1) != len(word2):
        return False

    # Convert the words to lists of characters
    word1_list = list(word1)
    word2_list = list(word2)

    # Sort the lists
    word1_list.sort()
    word2_list.sort()
    if word1_list == word2_list:
        return True
    else:
        return False
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if check_anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
