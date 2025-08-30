import re
paragraph = input("Enter paragraph: ")
words = re.findall(r'\w+', paragraph)
flag = False
for word in words:
    if word.lower() == word.lower()[::-1]:
        print(f"{word}, ", end="")
        flag = True
if not flag:
    print(0)