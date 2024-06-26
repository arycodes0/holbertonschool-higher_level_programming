#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError) as error:
            div = 0
            if isinstance(error, TypeError):
                print("wrong type")
            elif isinstance(error, ZeroDivisionError):
                print("division by 0")
            elif isinstance(error, IndexError):
                print("out of range")
        finally:
            new_list.append(div)
    return new_list
