# Kaivan Taylor
def loop_size(node):
    dict_index = {} # holds all positions of nodes and their position value
    i = 0   # start a position value 0

    while True:
        if node in dict_index:  # node has reached a marked node
            return i - dict_index[node]
        dict_index[node] = i    # set the position value for the node
        node = node.next    # look at pointer and go to next node
        i += 1  # counter +1 for every node traveled to
