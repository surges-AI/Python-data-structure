class s_stack:
    def __init__(self):
        self.stack=[]

    #判断是否为空
    def is_empty(self):
        return len(self.stack)==0

    #求栈长度
    def length(self):
        return len(self.stack)

    #遍历栈
    def travel(self):
        print(self.stack)

    #压栈
    def push(self,num):
        self.stack.append(num)

    #弹出
    def pop(self):
        self.stack.pop(len(self.stack)-1)

    #按索引查值
    def search(self,num):
        return self.stack[num]

    #按值查索引
    def get(self,num):
        return self.stack.index(num)

if __name__=='__main__':
    stack=s_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.travel()
    stack.pop()
    stack.travel()
    print(stack.get(3))
    print(stack.search(3))