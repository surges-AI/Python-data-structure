class s_queue:
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
        p=self.head
        for _ in range(self.size):
            item.append(self.data[p])
            p=(p+1)%self.num
        print(item)

    #入队
    def append(self,n):
        if self.size==self.num:
            print("队列已满")
            return
        self.size+=1
        self.data[self.tail]=n
        self.tail=(self.tail+1)%self.num

    #出队
    def pop(self):
        if self.is_empty():
            print("队列为空")
            return
        self.size-=1
        self.data[self.head]=None
        self.head=(self.head+1)%self.num

    #按值查索引
    def search(self,n):
        p=self.head
        r=0
        while r<self.size:
            if self.data[p]==n:
                return r
            p=(p+1)%self.num
            r+=1
        return -1

    #按索引查值
    def get(self,n):
        if n>=self.num or n<0 or n>=self.size:
            print("没有这个索引")
        return self.data[(self.head+n)%self.num]

if __name__=='__main__':
    queue=s_queue(6)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    queue.traval()
    print(queue.get(4))
    queue.pop()
    queue.traval()
    print(queue.length())
    print(queue.is_empty())
    print(queue.search(4))
