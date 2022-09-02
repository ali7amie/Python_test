def is_leap_year(year):
    
    c = [ year%4 == 0, year%100 == 0, year%400 == 0 ]

    if ( (c[0] and not(c[1])) or (c[0] and c[1] and c[2])):
        result = True
    else:
        result = False

    return result

         
          
