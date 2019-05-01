def create_phone_number(n):
    #print(n)
    holder1 = ''
    holder2 = ''
    holder3 = ''

    for x in n[0:3]:
        x = str(x)
        holder1 += str(x)

    for x in n[3:6]:
        x = str(x)
        holder2 += str(x)

    for x in n[6:10]:
        x = str(x)
        holder3 += str(x)

    final = ('({}) {}-{}'.format(holder1,holder2,holder3))

    return final
