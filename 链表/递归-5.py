a=list(range(20,0,-1))
b=[]
c=[]

def g(n):
    f(n,a,b,c)

def f(n:int,a:list,b:list,c:list):
    # 汉诺塔递归函数
    # 参数:
    # n: 要移动的盘子数量
    # a: 源柱子
    # b: 辅助柱子
    # c: 目标柱子
    # 基本情况：如果没有盘子需要移动，直接返回
    if n==0:
        return
    # 将n-1个盘子从a柱移动到b柱，c作为辅助
    f(n-1,a,c,b)
    # 打印移动操作（这里假设p()是一个打印函数）
    p()
    # 将最底层的盘子从a柱移动到c柱
    c.append(a.pop())
    # 将n-1个盘子从b柱移动到c柱，a作为辅助
    f(n-1,b,a,c)

def p():
    print(a)
    print(b)
    print(c)
    print("------------------------")

if __name__ == '__main__':
    g(20)
    p()