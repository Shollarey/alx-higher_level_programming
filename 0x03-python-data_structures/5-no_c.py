#!/usr/bin/python3

def no_c(my_string):
    str_list = []
    for i in my_string:
        str_list.append(i)
    while 'c' in str_list:
        str_list.remove('c')
    while 'C' in str_list:
        str_list.remove('C')
    new_str = ""
    for i in str_list:
        new_str += i
    return new_str
