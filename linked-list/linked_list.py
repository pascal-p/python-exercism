class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succ = succeeding
        self.prev = previous

    def __str__(self):
         return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.curr = None

    def unshift(self, elem):
        """
        insert elem at the front
        """
        node = Node(elem)
        node.succ = self.head
        if self.head != None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.length += 1
        return self

    def shift(self):
        """
        remove value at front
        """
        if self.is_empty():
            raise ValueError("Empty list")

        elem = self.head.value
        self.length -= 1
        # remove last element?
        if self.length == 0:
            self.head = self.tail = None
        else:
            self.head = self.head.succ
            self.head.prev = None
        return elem

    def push(self, elem):
        """
        insert value at the back
        """
        node = Node(elem)
        node.prev = self.tail
        if self.tail != None:
            self.tail.succ = node
        else:
            self.head = node
        self.tail = node
        self.length += 1
        return self

    def pop(self):
        """
        remove value at the back
        """
        if self.is_empty():
            raise ValueError("Empty list")
        elem = self.tail.value
        self.length -= 1
        if self.length == 0:
             self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.succ = None
        return elem

    def is_empty(self):
        return self.length == 0

    #
    # iterator
    #
    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty(): raise StopIteration()

        if self.curr != self.tail:
            if self.curr == None:
                self.curr = self.head
            else:
                self.curr = self.curr.succ
            return self.curr.value
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

    #
    # len
    #
    def __len__(self):
        return self.length

    def __str__(self):
        if self.head == None:
            return ''

        plst = self.head
        l = []
        while True:
            l.append(plst.value)
            plst = plst.succ
            if plst == None: break
        return ", ".join([str(e) for e in l])
