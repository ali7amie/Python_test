def rotate(text,key):

    result = ""
    for char in text: 

        # rotation on uppercase char
        if (char.isupper()):
            result = result + chr((ord(char) + key - 65) % 26 + 65)
  
        # rotation on lowercase char
        elif (char.islower()):
            result = result + chr((ord(char) + key - 97) % 26 + 97)

        # no rotation for other char, spaces, ponctuations...
        else:
            result = result + char    
  
    return result