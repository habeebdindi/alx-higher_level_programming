def only_diff_elements(set_1, set_2):
    stp1 = set_1.difference(set_2)
    stp2 = set_2.difference(set_1)
    fin = stp1.union(stp2)
    return fin
