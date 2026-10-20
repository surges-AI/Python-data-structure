class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class s_list:
    def __init__(self, node=None):
        self.head = node

    #判断是否为空
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # 求链表长度
    def length(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            p = self.head
            while p.next is not None:
                count += 1
                p = p.next
            return count

    # 遍历链表
    def travel(self):
        if self.is_empty():
            print("[]")
            return
        p = self.head
        print("[", end="")
        while (p != None):
            print(f" {p.value}", end="")
            if (p.next is not None):
                print(",", end="")
            p = p.next
        print(" ]")

    # 头部添加元素
    def add(self, num):
        p = Node(num)
        p.next = self.head
        self.head = p

    # 尾部添加元素
    def append(self, num):
        if (self.is_empty()):
            self.add(num)
            return
        p = Node(num)
        q = self.head
        while q.next is not None:
            q = q.next
        q.next = p

    #指定位置添加元素
    def insert(self, pos, num):
        if (pos > self.length() or pos < 0):
            print("没有这个索引")
            return
        if (pos == 0):
            self.add(num)
            return
        if (pos == self.length()):
            self.append(num)
            return
        p = Node(num)
        q = self.head
        i = pos - 1
        while i > 0:
            q = q.next
            i = i - 1
        p.next = q.next
        q.next = p

    #头部删除元素
    def popleft(self):
        if self.length()==0:
            print("链表为空")
            return
        self.head=self.head.next

    #尾部删除元素
    def pop(self):
        if self.is_empty():
            print("空表保护")
            return
        if self.length() == 1:
            self.head = None
            return
        p = self.head
        while p.next.next is not None:
            p = p.next
        p.next = None

    #按索引删值
    def remove(self, num):
        if (num >= self.length() or num < 0):
            print("没有这个索引")
            return
        if (num == 0):
            self.head = self.head.next
            return
        p = self.head
        i = num - 1
        while i > 0:
            p = p.next
            i -= 1
        p.next = p.next.next

    #按索引查值
    def get(self,num):
        k=i=0
        p=self.head
        while i < num:
            i+=1
            p=p.next
        return p.value

    #按值查索引
    def search(self,num):
        p=self.head
        i=0
        while p is not None:
            if p.value==num:
                return i
            i+=1
            p=p.next
        return -1

    #按值删索引
    def remove_value(self,num):
        if self.get(self.length()-1)==num:
            self.pop()
            return
        if self.head==num:
            self.head=self.head.next
            return
        p=self.head
        while p is not None and p.next is not None:
            if p.next.value==num:
                p.next=p.next.next
                return
            p=p.next
        return

    #反转链表
    def reverse(self):
        if self.head is None and self.head.next is not None:
            return
        p=None
        q=k=self.head
        while q is not None:
            q=q.next
            k.next=p
            p,k=k,q
        self.head=p
        return

    #清空链表
    def clean(self):
        self.head=None

if __name__ == "__main__":
    list=s_list()
    list.travel()
    list.add(1)
    list.add(2)
    list.add(3)
    list.travel()
    list.pop()
    list.travel()
    list.insert(1, 4)
    list.travel()
    list.reverse()
    list.travel()
    print(list.get(2))
    print(list.search(4))
    list.remove_value(4)
    list.remove(1)
    list.travel()
    print(list.length())
    list.clean()
    list.travel()