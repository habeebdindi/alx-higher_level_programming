def only_diff_elements(set_1, set_2):
    stp1 = set_1 - set_2
    stp2 = set_2 - set_1
    fin = stp1 | stp2
    return fin
