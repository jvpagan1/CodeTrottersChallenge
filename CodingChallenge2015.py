def int_to_word(i1):
    result =""
    i=i1
    d = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
    11:"eleven",12:"twelve",13:"thirteen",14:"forteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
    20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
    100:"hundred",1000:"thousand",1000000:"million"}
    
    #Split integer into three numbers: first 3 digits (left to right), 2nd 3 digits, and last 3 digits
    #Loop extracts the a new 3 digit number from the integer for every n.
    for n in range(3):
        u = 10**(n*3) # (1, 1000, 1000000) used to divide integer to extract first, second and third number.
    
        if i > u: #If number is less than u, end.
            #Extract next 3 digit number and separate digits into hundreds, tens and ones.
            number = i/u%1000 #extract next 3 digit number
            hundreds = number/100
            tens = number%100/10
            ones = number%10

            #Convert first two digits: tens and ones           
            if tens == 0 and ones == 0:
                result1 = ""
            if tens == 0 and ones > 0:
                result1 = d[ones]
            if tens == 1:
                result1 = d[tens*10+ones]
            if tens > 1 and ones == 0:
                result1 = d[tens*10]
            if tens > 1 and ones > 0:
                result1 = d[tens*10] + " " + d[ones]

            #Add third digit with word hundreds
            if hundreds >0:
                if result1 == "":  #If first two digits are zeroes, result1 = hundreds, else add to first two digits
                    result1 = d[hundreds] + " " + d[100]
                else:
                    result1 = d[hundreds] + " " + d[100] + " " + result1
            if u>1 and number >0:
                result1 = result1 + " " + d[u]
            #If 3 digit number is not zero, add it to result (word) 
            if result1 != "":
                result = result1 + " " + result
        else:
            break
    if result !="":
        return result
    else:
        return "zero"

#for s in xrange(1000000000):
#    print int_to_word(s)
print int_to_word(2334235)
        