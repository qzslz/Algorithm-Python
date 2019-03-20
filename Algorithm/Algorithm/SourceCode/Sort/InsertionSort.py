"""
插入排序
"""

def insertion_sort(list):

    list_len = len(list)

    for i in range(0,list_len):
        pre_index = i-1
        for j in range(0,i+1):
            if pre_index >= 0 and list[pre_index+1] < list[pre_index]:
                list[pre_index],list[pre_index+1] = list[pre_index+1],list[pre_index]
                pre_index -= 1
                continue
            break
    return list

array = [2,3,4,5,6,7,8,10,1,9,4]
print(insertion_sort(array))