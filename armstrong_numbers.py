def is_armstrong(number):
    ''' 
    This function takes a number, computes its narcissistic sum, and returns whether it is an Armstrong number or not 

    parameters:
    -------------
    number: int   
       
    Return:
    -------  
    result: bool

    '''

    digit = len(str(number))
    sum=0
    for i in range(0,len(str(number))):
        sum = sum + int(str(number)[i])**digit

    return sum==number  
