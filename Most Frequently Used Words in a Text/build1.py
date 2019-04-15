# text = '''In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.'''
text = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

txtsplit = text.split()
#print(txtsplit)

txtdic = {}

for str in txtsplit:
    if str in txtdic:
        txtdic[str] = txtdic[str] + 1
    else:
        txtdic[str] = 1
print(txtdic)
list = []
for i in txtdic:
    list.append((txtdic[i],i))

list.sort()
#list.reverse()
print(list)

number = 0
final = {}
