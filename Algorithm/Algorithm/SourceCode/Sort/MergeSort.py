"""
归并排序

"""

def merge_sort(array):
    """
    接受一个乱序数组
    :param array:
    :return: 返回一个有序数组
    """
    if array.__len__() == 1:
        return array
    elif array.__len__() == 2:
        return array if array[0] < array[1] else [array[1],array[0]]
    else:
        middleIndex = int(array.__len__()/2)
        return mergeArray(merge_sort(array[0:middleIndex]),merge_sort(array[middleIndex:]))

def mergeArray(arr1,arr2):
    """
    传入两个需要合并的数组
    :param arr1:
    :param arr2:
    :return: 返回一个有序数组
    """
    tempArray = []
    for _ in range(0,arr1.__len__()+arr2.__len__()):
        if arr1.__len__() == 0:
            tempArray.append(arr2.pop(0))
        elif arr2.__len__() == 0:
            tempArray.append(arr1.pop(0))
        else:
            if arr1[0] > arr2[0]:
                tempArray.append(arr2.pop(0))
            else:
                tempArray.append(arr1.pop(0))
    return tempArray

sortArray = [8,4,5,7,10,1,3,6,2,1]
print(merge_sort(sortArray))