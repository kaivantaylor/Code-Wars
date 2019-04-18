# Kaivan Taylor
# Summary - This time no story, no theory. The examples below show you how to
# write the function accum
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The paramter of accum is a string which includs only letters from
# a..z and A..Z

import re

test1 = ("abcd") # "A-Bb-Ccc-Dddd"
test2 = ("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
test3 = ("cwAt") # "C-W-Aaa-Tttt"

def accum(text):
    str_holder = text.lower().strip()
    answer = ''
    
    counter = 0
    
    for x in str_holder:
        print(x)
        print(counter)
        if counter == 0:
            print(x.upper())
            
            opt1 = x.upper()
            answer += opt1
            
            
        else:
            print((str("-" + x.upper() + str(x*counter))))
            opt2 = (str("-" + x.upper() + str(x*counter)))
            answer += opt2
        counter += 1
        

    return answer

    
    




