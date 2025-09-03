def  convert2binary(num:int) ->str:  
    result = "" 
    while num >0 : 
        if num%2 ==1:
            result = result +"1" 
        else : 
            result = result + "0" 
        num = num //2 
    result = result[::-1] 
    return result 


a = print(convert2binary(12))
