class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class s_list:
    def __init__(self):
        self.s=Node()
        self.s.next=self.s
        self.s.prev=self.s
        self.s_length=0

    # 判断是否为空
    def is_empty(self):
        return self.s_length == 0

    # 求链表长度
    def length(self):
        return self.s_length

    # 遍历链表
    def travel(self):
        p=self.s.next
        if self.is_empty():
            print("[]")
            return
        print("[", end="")
        while p is not self.s:
            print(f" {p.value}", end="")
            if p.next is not self.s:
                print(",", end="")
            p=p.next
        print(" ]")

    # 头部添加元素
    def add(self,num):
        p=Node(num)
        p.next=self.s.next
        p.prev=self.s
        self.s.next.prev=p
        self.s.next=p
        self.s_length+=1

    # 尾部添加元素
    def append(self,num):
        if self.s_length==0:
            self.add(num)
            return
        p=Node(num)
        q=self.s.next
        while q.next is not self.s:
            q=q.next
        p.next = q.next
        p.prev = q
        q.next.prev = p
        q.next = p
        self.s_length += 1

    # 指定位置添加元素
    def insert(self,pos,num):
        if self.s_length < pos or 0 > pos:
            print("没有这个索引")
            return
        if pos == 0:
            self.add(num)
            return
        p = Node(num)
        q = self.s.next
        i = 0
        while i + 1 != pos:
            i+=1
            q=q.next
        p.next = q.next
        p.prev = q
        q.next.prev = p
        q.next = p
        self.s_length += 1

    # 尾部删除元素
    def pop(self):
        if self.s_length == 0:
            print("列表为空")
            return
        q = self.s
        while q.next.next is not self.s:
            q = q.next
        q.next=q.next.next
        q.next.prev=q
        self.s_length -= 1

    # 指定位置删除元素
    def remove(self,pos):
        if self.s_length-1 < pos or 0 > pos:
            print("没有这个索引")
            return
        if self.s_length == 0:
            print("列表为空")
            return
        if pos == 0:
            self.s.next=self.s.next.next
            self.s.next.prev=self.s
            self.s_length -= 1
            return
        q = self.s.next
        i = 0
        while i + 1 != pos:
            i += 1
            q = q.next
        q.next = q.next.next
        q.next.prev = q
        self.s_length -= 1

if __name__ == "__main__":
    list=s_list()
    list.append(0)
    list.travel()
    list.add(1)
    list.add(2)
    list.add(3)
    list.travel()
    list.pop()
    list.append(5)
    list.travel()
    list.insert(1, 4)
    list.travel()
    list.remove(1)
    list.travel()
    print(list.length())