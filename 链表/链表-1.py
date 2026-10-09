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

    #指定位置删除元素
    def remove(self, num):
        if (num > self.length() or num < 0):
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
    list.remove(1)
    list.travel()
    print(list.length())