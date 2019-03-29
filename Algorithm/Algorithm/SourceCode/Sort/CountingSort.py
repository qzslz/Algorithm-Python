"""
计数排序
"""

def counting_sort(array):
     n=len(array)
     b=[None]*n
     for i in range(n):
          p=0
          q=0
          for j in range(n):
               if array[j]<array[i]:
                    p+=1
               elif array[j]==array[i]:
                    q+=1
          for k in range(p,p+q):
               b[k]=array[i]
     return b


sortArray = [-1,-3,-3,2,1]
print(counting_sort(sortArray))