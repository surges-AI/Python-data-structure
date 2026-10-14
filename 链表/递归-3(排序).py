def sort(a:list):
    bubble(a,len(a))

def bubble(a:list,j):
    """
    这是一个冒泡排序的递归实现函数
    :param a: 待排序的列表
    :param j: 列表中需要进行排序的元素个数
    """
    if 1 == j:  # 递归的基准情况，当需要排序的元素个数为1时，直接返回
        return
    x=0  # 记录最后一次交换的位置，用于优化递归范围
    for i in range(j-1):
        if a[i] > a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]   # 交换相邻元素，将较大的元素向后移动
            x=i  # 更新最后一次交换的位置
    bubble(a,x)  # 对已排序部分之前的部分进行递归排序

def inserting(a:list,j=1):

    """
    插入排序的递归实现函数
    参数:
        a: 待排序的列表
        j: 当前已排序部分的末尾索引
    """
    if j == len(a):  # 递归终止条件：当j等于列表长度时，说明所有元素已排序完毕
        return
    t=a[j]  # 保存当前待插入元素的值
    i=j-1  # 从已排序部分的最后一个元素开始比较
    while i >= 0 and a[i] > t:  # 将大于待插入元素的元素向后移动
        a[i+1]=a[i]
        i-=1
    a[i+1]=t  # 将待插入元素放到正确的位置
    inserting(a,j+1)  # 递归处理下一个元素

if __name__ == '__main__':
    a=[9,8,7,6,5,4,3,2,1]
    inserting(a)
    print(a)