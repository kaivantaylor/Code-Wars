def pig_it(text):
    #str_test = 'hello my name is kaivan'
    # print(str_test.split()) ['hello', 'my', 'name', 'is', 'kaivan']

    list_holder = text.split()
    # print(list_holder) ['hello', 'my', 'name', 'is', 'kaivan']
    list_holder.reverse()
    # print(list_holder) ['kaivan', 'is', 'name', 'my', 'hello']

    # trying to pop the list and then grab each index at a time
    str_ending = "ay" # Words will always end with ay in pig latin
    list_output = []
    while len(list_holder) != 0:
        # print(len(list_holder))
        # print('')
        word_holder = list_holder.pop()
        # After getting the word, we need to filter any numbers and punctuation
        if word_holder.isalpha() == False:
            #print("is a digit, or puntuation")
            list_output.append(word_holder)
            break

        # print(word_holder) (1) hello (2) my (3) name (4) is (5) kaivan
        # print(word_holder[0]) # first letter
        # print(word_holder[1:]) # letters after the first word
        # print(word_holder[1:] + word_holder[0] + str_ending) # pig latin word
        str_word = word_holder[1:] + word_holder[0] + str_ending
        list_output.append(str_word)

    # print(list_holder) # Should be an empty list after all of the interations have passed
    # print(list_output)
    # print (' '.join(list_output))
    output = ' '.join(list_output)

    return output
