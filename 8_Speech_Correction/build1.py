# Kaivan Taylor
# Cases that need to be switched if found in string
# are - aren't
# can - can't
# could - couldn't
# did - didn't
# do - don't
# had - hadn't
# has - hasn't
# have - haven't
# is - isn't
# might - mightn't
# must - mustn't
# should - shouldn't
# was - wasn't
# were - weren't
# would - wouldn't

# imports
import re

# testing..
poscases = {'are','can','could'}
blankcases = {}
singlecases = {'can'}
testpos = 'are'
teststr = 'My name can CAN be Kaivan'

print(teststr)

if testpos in poscases:
    #print("Exists.")
# we can use bool(words) to check if it is empty

if (bool(poscases)):
    #print("There is no blanks in the current set.")
    str_re = set(re.findall(r"(?=("+'|'.join(singlecases)+r"))",teststr.lower())) # make a set to remove duplicates
    #print(r"("+'|'.join(poscases)+")")
    print(str_re)

    new_str = ''
    for x in str_re:
        # we have to try making x.lower() and x.upper() for duplicates
        up_x = x.upper()
        lo_x = x.lower()

        teststr = teststr.replace(lo_x, lo_x +"'t")
        teststr = teststr.replace(up_x, up_x +"'T")

        # print(x)
        # if x.islower():
        #     print("lowercase letter")
        #     new_str += teststr.replace(x, x +"'t")
        # else:
        #     print("captial letter")
        #     new_str += teststr.replace(x, x.upper() +"'T")
        print(teststr)

else:
    print(teststr)
