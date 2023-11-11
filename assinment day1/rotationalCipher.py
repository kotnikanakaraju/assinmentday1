def rotationalCipher(text,key):
    raju=''
    for char in text:
        if char.isalpha():
            if char.islower():
                raju+=chr((ord(char)-97+key)%26+97)
            else:
                raju+=chr((ord(char)-65+key)%26+65)
        else:
            raju+=char
    return raju

if __name__ == '__main__':
    text=input()
    key=int(input())
    print(rotationalCipher(text,key))
    