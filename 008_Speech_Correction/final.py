# Kaivan Taylor
# Final build

# imports
import re
def speech_correction(words, speech):
    cases = words
    str_speech = speech

    if (bool(cases)):
        #print("There is no blanks in the current set.")
        str_re = set(re.findall(r"(?=("+'|'.join(cases)+r"))",str_speech.lower())) # make a set to remove duplicates
        #print(str_re)

        for x in str_re:
            # we have to try making x.lower() and x.upper() for duplicates
            up_x = x.upper() # i.e. CAN
            lo_x = x.lower() # i.e. can

            str_speech = str_speech.replace(lo_x, lo_x +"n't") # might want to use re for this as well
            str_speech = str_speech.replace(up_x, up_x +"N'T")
            #print(str_speech)
        return str_speech

    else:
        return str_speech
