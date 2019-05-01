# Kaivan Taylor
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with out own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

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
