class s_deque:
    def __init__(self,num):
        self.size=0
        self.head=0
        self.tail=0
        self.data=[None]*num
        self.num=num

    #判断是否为空
    def is_empty(self):
        return self.size==0

    #求队列长度
    def length(self):
        return self.size

    #遍历队列
    def traval(self):
        item=[]
        i=self.head
        for _ in range(self.size):
            item.append(self.data[i])
            i=(i+1)%self.num
        return item

    #头部入队
    def add(self,n):
        self.head=(self.head+self.num-1)%self.num
        self.data[self.head]=n
        self.size+=1

    #尾部入队
    def append(self,n):
        self.data[self.tail]=n
        self.tail=(self.tail+1)%self.num
        self.size += 1

    #头部出队
    def popleft(self):
        n=self.data[self.head]
        self.data[self.head]=None
        self.head=(self.head+1)%self.num
        self.size -= 1
        return n

    #尾部出队
    def pop(self):
        n=self.data[(self.tail+self.num-1)%self.num]
        self.data[(self.tail+self.num-1)%self.num]=None
        self.tail=(self.tail+self.num-1)%self.num
        self.size -= 1
        return n

    #查头部元素
    def d_head(self):
        return self.data[self.head]

    #查尾部元素
    def d_tail(self):
        return self.data[(self.tail+self.num-1)%self.num]

if __name__=='__main__':
        deque=s_deque(5)
        deque.add(2)
        deque.add(1)
        deque.append(3)
        deque.append(4)
        deque.append(5)
        print(deque.traval())
        deque.pop()
        deque.popleft()
        print(deque.traval())
        print(deque.d_head())
        print(deque.d_tail())