import string

def top_3_words(text):
    txtsplt = text.split()
    #print(txtsplt)

    list = []

    for x in txtsplt:
        x = x.lower()
        #print(lower_x)
        x = x.strip(string.punctuation)
        #print(x)
        list.append(x)
    #print(list)

    dict = {}

    for x in list:
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = int(1)
    newlist= []
    for x in dict:
        newlist.append((dict[x],x))

    newlist.sort()
    newlist.reverse()
    final = []
    count = 0
    for x in newlist:
        if count < 3:
            if x[1] != '':
                final.append(x[1])
                count += 1
    return final
print(top_3_words("ef  ei si se :e fesfs ax d s s d d s fe fag a se sd c"))
