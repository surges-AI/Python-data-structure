def f(a:list,target,i,j):
    """
    这是一个二分查找的递归实现函数，用于在有序列表中查找目标值的位置
    参数:
        a: 有序列表，类型为list
        target: 要查找的目标值
        i: 查找范围的起始索引
        j: 查找范围的结束索引
    返回值:
        如果找到目标值，返回其索引位置
        如果未找到目标值，返回-1
    """
    if i > j:
        return -1
    s=(i+j)//2
    if target < a[s]:
        return f(a,target,i,s-1)
    elif target > a[s]:
        return f(a,target,s+1,j)
    else:
        return s

if __name__ == '__main__':
    print(f([1,2,3,4,5,6],4,0,len([1,2,3,4,5,6])-1))