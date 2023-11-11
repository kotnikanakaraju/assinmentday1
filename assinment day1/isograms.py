words=input()
def isogram(words):
    words=words.lower()

    stack=[]
    for letter in words:
        if letter in stack:
            return False
        stack.append(letter)
    return True
print(isogram(words))