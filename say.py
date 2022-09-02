def thousands_division(number):

    string=str(number)
    if len(string) > 3:

        #devide the string into residual and main parts
        residual_string_length=len(string)%3
        residual_string=[string[0:residual_string_length]]

        main_string_length=len(string)-residual_string_length
        main_string=[]
        for i in range(residual_string_length,len(string),3):
            main_string.append(string[i:i+3])
    
        #concatenate the two string
        number_list=residual_string+main_string

        return number_list
    
    if len(string) > 12:
        return print('Out of range')
    
    if len(string) < 4:
        number_list=[string]
        return number_list



def words(num):

    string=str(num)

    below_ten = ["", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
  
    ten_to_twenty = ["","ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
  
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]
  
    if (len(string) > 12):
        return "out of range"
 
    #empty string
    if len(string) == 0:
        return ""

    # 1 digit string
    if len(string) == 1:
        if int(string)==0:
            return "zero"
        else:  
            return below_ten[int(string[0])] 

    # 2 digit string
    if len(string) == 2 and int(string[0])==1:
        return ten_to_twenty[1:11][int(string[1])]
    
    if len(string) == 2 and int(string[0])!=1:
        return tens_multiple[int(string[0])]+ " " +below_ten[int(string[1])]        
    
    # 3 digit string
    if len(string) == 3 and int(string[1]) == 1:
        return  below_ten[int(string[0])]+ ' ' + 'hundred' + ' ' + ten_to_twenty[1:11][int(string[2])] 

    if len(string) == 3 and int(string[1]) != 1:
        return  below_ten[int(string[0])]+' ' + 'hundred' + ' ' + tens_multiple[int(string[1])]+ ' ' + below_ten[int(string[2])]  



def say(num):
     
    if len(str(num)) > 12:
        return print('Out of range')

    else:
        number_list=thousands_division(num)



        extension=['billions','millions','thousands','']
        combining_list = []

        for i in range(1,len(number_list)+1):
            if len(number_list[-i]) != 0:
                combining_list.append(words(number_list[-i])+ ' ' + extension[-i])

        combining_list = list(reversed(combining_list))

        num_words = ''
        for i in range(0,len(combining_list)):
            num_words = ' ' + num_words + ' ' + combining_list[i]    

    

        return num_words

        