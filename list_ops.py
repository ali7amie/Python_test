
def append(xs, ys):
  return xs+ys
    


def concat(lists):
    concatenated_list=[]
    for i in lists:
      concatenated_list=concatenated_list+i
    return concatenated_list  


def filter_clone(function, xs):
    final_list=[]
    for x in xs:
      if function(x)==True:
        final_list=final_list+[x]
    return final_list


def length(xs):
    s=0
    for i in xs:
        s=s+1
    return s    


def map_clone(function, xs):
    final_list=[]
    for x in xs:
      final_list=final_list+[function(x)]
    return final_list  


def foldl(function, xs, acc):
    if len(xs)!=0:
        result=function(acc,xs[0])
        for i in range(1,len(xs)):
            result=function(result,xs[i])
        return result  
    else:
        return acc   
      



def foldr(function, xs, acc):
    if len(xs)!=0:
        result=function(xs[0],xs[1])
        xs=xs+[acc]
        for i in range(len(xs)-2,0,-1):
            result=function(result,xs[-i])
        return result 
    else:
        return acc         
       

def reverse(xs):
    reversed_list=[]
    for i in range(len(xs)-1,-1,-1):
      reversed_list=reversed_list+[xs[i]]
    return reversed_list  
