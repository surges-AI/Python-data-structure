def f(n):
    """
    计算给定整数n的阶乘
    使用递归方式实现
    参数:
        n: 需要计算阶乘的正整数
    返回:
        n的阶乘结果
    """
    if n == 1:
        return 1
    return n*f(n-1)

def s(h,i=0):  # 定义一个递归函数s，接收一个参数h和一个可选参数i，默认值为0
    if i == len(h):  # 递归终止条件：当i等于h的长度时，结束递归
        return  # 返回空，结束当前递归调用
    s(h,i+1)  # 递归调用函数s，参数为h和i+1，继续处理下一个字符
    print(h[i],end="")  # 打印当前字符，end=""表示不换行


if __name__=='__main__':
    print(f(6))
    s("abcdefg")