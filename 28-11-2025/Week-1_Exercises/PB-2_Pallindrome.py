word=input("Enter your word: ")
word1=word.lower()
reverse=word1[::-1]
if word1==reverse:
    print("It's a palindrome")
else:
    print("Not a palindrome")