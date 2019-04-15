import string
def top_3_words(text):
    txtsplt = text.split()
    #print(txtsplt)

    dict = {}

    for x in txtsplt:
        x = x.lower()
        #print(lower_x)
        x = x.strip(string.punctuation)
        #print(x)

        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = int(1)

    list = []
    for x in dict:
        list.append((dict[x],x))
    list.sort()
    list.reverse()

    final = []
    count = 0
    for x in list:
        if count < 3:
            if x[1] != '':
                final.append(x[1])
                count += 1

    return final
