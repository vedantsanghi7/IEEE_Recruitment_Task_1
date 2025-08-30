import re
paragraph = input("Enter paragraph: ")

# Extract words from the paragraph without punctuation
words = re.findall(r'\w+', paragraph)

# flag used to check if any palindrome is found
flag = False
for word in words:
    if word.lower() == word.lower()[::-1]:
        print(f"{word}, ", end="")
        flag = True
if not flag:
    print(0)