# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word_lower = word.lower()
    anagram_lower = anagram.lower()

    if (len(word_lower) == len(anagram_lower)):
        word_lower_sorted = sorted(word_lower)
        anagram_lower_sorted = sorted(anagram_lower)

        if word_lower_sorted == anagram_lower_sorted:
            return True

        else:
            return False
    else:
        
        return False

print(find_anagram("race", "care"))
print(find_anagram("hello", "Check"))
