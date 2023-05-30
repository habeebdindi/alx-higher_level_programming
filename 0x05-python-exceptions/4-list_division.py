#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new, typ = [], [int, float]
    if len(my_list_1) <= 0 or len(my_list_2) <= 0 or list_length <= 0:
        print("out of range")
        return
    try:
        for i in range(list_length):
            if type(my_list_1[i]) in typ and type(my_list_2[i]) in typ:
                try:
                    new.append(my_list_1[i] / my_list_2[i])
                except (TypeError, ValueError) as ze:
                    new.append(0)
                    print("division by 0")
            else:
                new.append(0)
                print("wrong type")
    except (TypeError, ValueError) as e:
        pass
    finally:
        return new
