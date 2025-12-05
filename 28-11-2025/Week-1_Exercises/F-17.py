
import re

def longest_word(sentence):
    # Split on non-letters to ignore punctuation; keep apostrophes if you like
    words = re.findall(r"[A-Za-z']+", sentence)
    if not words:
        return None
    return max(words, key=len)

print(longest_word("Find the longest word, perhaps 'extraordinary'!"))

