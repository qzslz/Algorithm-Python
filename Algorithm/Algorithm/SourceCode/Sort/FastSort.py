"""
快速排序
"""

def fast_sort(array):
    if array.__len__() == 0 or array.__len__() == 1:
        return array
    else:
        temp = array[0]
        i = 0
        j = array.__len__() - 1

        direction = False

        while True:
            if i == j:
                tempValue = array[0]
                array[0] = array[j]
                array[j] = tempValue
                if i > 1: array[0:i] = fast_sort(array[0:i])
                if i < array.__len__()-1: array[i+1:] = fast_sort(array[i+1:])
                break
            else:
                if direction:  # 顺序查找
                    if array[i] > temp:
                        tempValue = array[i]
                        array[i] = array[j]
                        array[j] = tempValue
                        direction = not direction
                        continue
                    i += 1
                else:  # 倒序查找
                    if array[j] < temp:
                        direction = not direction
                        continue
                    j -= 1

    return array


sortArray = [72,6,57,88,60,42,83,73,48,85,42]
print(fast_sort(sortArray))