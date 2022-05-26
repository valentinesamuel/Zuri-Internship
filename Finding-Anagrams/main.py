# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    if len(word) == len(anagram):

        sorted_anagram = sorted(anagram)
        sorted_word = sorted(word)

        if sorted_anagram == sorted_word:
            print("anagrams")
            return True
        else:
            print("not anagrams")
            return False

    else:
        print("not anagrams")
        return False


