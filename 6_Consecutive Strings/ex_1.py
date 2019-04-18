def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            #print(s)
            if len(s) > len(result):
                result = s
    #print(len(strarr), len(strarr) - k + 1, strarr[index:index+k])
    return result

#print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 2))
