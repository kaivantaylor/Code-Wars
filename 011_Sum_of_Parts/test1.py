def parts_sums(ls):

    ls_holder = ls
    count = len(ls_holder)
    returned_ls = []

    print(ls_holder,count)

    while count >= 0:
        count -= 1
        ls_sum = sum(ls_holder)
        returned_ls.append(ls_sum)
        ls_holder = ls_holder[1:]

    return returned_ls
# Not Optimized
