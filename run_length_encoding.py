def encode(string):
    encoded_string = ""
    i = 0
 
    while (i <= len(string)-1):
        count = 1
        char = string[i]
        j = i
        while (j < len(string)-1):
            if (string[j] == string[j+1]):
                count = count+1
                j = j+1
            else:
                break
        if count==1:  
            encoded_string=encoded_string+char
            i = j+1
        if count > 1:    
            encoded_string=encoded_string+str(count)+char
            i = j+1
    return encoded_string



def decode(string):
    decoded_string = ""
    for i in range(0,len(string)):
      if string[i].isdigit() and not(string[i+1].isdigit()) and int(string[i])>1:
          for j in range(0,int(string[i])-1):
              decoded_string=decoded_string + string[i+1]
      if string[i].isdigit() and string[i+1].isdigit():  
          for j in range(0,int(string[i]+string[i+1])-1):
              decoded_string=decoded_string + string[i+2]  
      else:
          decoded_string=decoded_string+string[i] 
      decoded_string = ''.join(k for k in decoded_string if not k.isdigit())       
    return decoded_string