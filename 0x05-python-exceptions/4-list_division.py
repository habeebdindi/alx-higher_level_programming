#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    try:
        for i in range(list_length):
            try:
                new.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError as ze:
                print("division by 0")
                new.append(0)
            except (TypeError, ValueError):
                new.append(0)
                print("wrong type")
            except IndexError:
                new.append(0)
                print("out of range")
    except Exception as e:
        pass
    finally:
        return new
