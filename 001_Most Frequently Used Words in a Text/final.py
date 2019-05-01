import string
import re

def top_3_words(text):
    print(text)
    txtsplt = re.findall(r"[a-zA-Z']+|['a-zA-Z]+", text)
    #print(txtsplt)

    list_1 = []
    list_2= []
    list_final = []
    count = 0
    dict = {}
    words = 'bcdfghjklmnpqrstvxzaeiou'
    strip = r'!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

    for x in txtsplt:
        if  (any(c in words for c in x.lower()) == True):
            #print(x)
            x = x.lower()
            #print(lower_x)
            x = x.strip(strip)
            #print(x)
            list_1.append(x)
    #print(list_1)

    for x in list_1:
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = int(1)
    print(dict)

    for x in dict:
        list_2.append((dict[x],x))

    list_2.sort()
    list_2.reverse()
    list_2 = list_2[0:3]

    print(list_2)
    b = "''"
    new = []
    for x in list_2:
        a = x[1]
        new.append(a)
    #print(new)
    return new

print(top_3_words("das' das das ye's 'yes 'yes"))
