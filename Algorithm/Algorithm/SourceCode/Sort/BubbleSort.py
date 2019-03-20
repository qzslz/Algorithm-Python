"""
冒泡排序
"""

def bubble_sort(list):
    list_len = len(list)
    for i in range(0,list_len):
        for j in range(i+1,list_len):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list


array = [2,3,4,5,6,7,8,10,1,9,3]
print(bubble_sort(array))