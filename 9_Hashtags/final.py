def generate_hashtag(s):
    if s != '' and (len(s) <= 140):
        str_split = s.split()
        answer = '#'
        for x in str_split:
            hold = []
            # print('----------')
            # print(x[0])
            # print(x.isdigit())
            # print(x)
            if not x.isdigit():
                # print("This is not a digit")
                # print("-> joining: " + x[0].upper() + x[1:])
                hold += x[0].upper() + x[1:].lower()
                # print(hold)
                answer += "".join(hold)
            else:
                answer += x
        return answer
    else:
        return False

test1 = 'Code wars Kata 59'
test2 = ''
print(generate_hashtag(test1))
