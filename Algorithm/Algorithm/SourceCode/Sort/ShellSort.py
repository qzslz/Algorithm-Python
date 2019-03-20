"""
希尔排序
"""

import math

def shell_sort(list):
    list_len = len(list)
    if list_len == 1 or list_len == 0:
        return  list
    if list_len == 2:
        return list if list[0] < list[1] else [list[1],list[0]]
    else:
        increment = int(math.floor(float(list_len)/3)) + 1
        while increment >= 1:
            for i in range(0,list_len):
                pre_index = i-1
                for j in range(0,i+1):
                    if pre_index >= 0 and pre_index+increment < list_len and list[pre_index+increment] < list[pre_index]:
                        list[pre_index],list[pre_index+increment] = list[pre_index+increment],list[pre_index]
                        pre_index -= increment
                        continue
                    break
            if increment == 1:
                break
            increment = int(float(increment)/3) + 1
    return list

sortArray = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
print(shell_sort(sortArray))