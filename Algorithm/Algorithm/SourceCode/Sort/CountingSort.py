"""
计数排序
"""

def counting_sort(array):
    n = len(array)
    res = [None] * n
    # 首次循环遍历, 每个列表的数都统计
    for i in range(n):
        # p 表示 a[i] 大于列表其他数 的次数
        p = 0
        # q 表示 等于 a[i] 的次数
        q = 0
        # 二次循环遍历, 列表中的每个数都和首次循环的数比较
        for j in range(n):
            if array[i] >= array[j]:
                p += 1
            elif array[i] == array[j]:
                q += 1
        for k in range(p, p+q):  # q表示 相等的次数,就表示, 从 P 开始索引后, 连续 q 次,都是同样的 数
            res[k] = array[i]
    return res


sortArray = [72,6,57,88,60,42,83,73,48,85,42]
print(counting_sort(sortArray))