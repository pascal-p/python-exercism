class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self._value = value
        self._succ = succeeding
        self._prev = previous

    def value(self):
        return self._value

    def succ(self):
        return self._succ

    def prev(self):
        return self._prev

    def __str__(self):
         return f"{self._value}"


class EmptyListException(Exception):
    pass


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._curr = None

    def head(self):
        if self.is_empty():
            raise EmptyListException()
        return self._head

    def tail(self):
        if self.is_empty():
            raise EmptyListException()
        return self._tail

    def unshift(self, elem):
        """
        insert elem at the front
        """
        node = Node(elem)
        node._succ = self._head
        if self._head != None:
            self._head._prev = node
        else:
            self._tail = node
        self._head = node
        self._length += 1
        return self

    def shift(self):
        """
        remove value at front
        """
        if self.is_empty():
            raise EmptyListException()

        node = self._head
        self._length -= 1
        # remove last element?
        if self._length == 0:
            self._head = self._tail = None
        else:
            self._head = self._head._succ
            self._head._prev = None
        node._succ = node._prev = None
        return node._value

    def push(self, elem):
        """
        insert value at the back
        """
        node = Node(elem)
        node._prev = self._tail
        if self._tail != None:
            self._tail._succ = node
        else:
            self._head = node
        self._tail = node
        self._length += 1
        return self

    def pop(self):
        """
        remove value at the back
        """
        if self.is_empty():
            raise EmptyListException()
        node = self._tail
        self._length -= 1
        if self._length == 0:
             self._head = self._tail = None
        else:
            self._tail = self._tail._prev
            self._tail._succ = None
        node._succ = node._prev = None
        return node._value

    def is_empty(self):
        return self._length == 0

    #
    # iterator
    #
    def __iter__(self):
        return self

    def __next__(self):
        """
        'natural' order from head to tail
        """
        if self.is_empty(): raise StopIteration()

        if self._curr != self._tail:
            self._curr = self._head if self._curr == None else self._curr._succ
            return self._curr._value
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

    def __reversed__(self):
        """
        reverse order from tail to head...
        """
        if self.is_empty(): raise StopIteration()

        if self._curr != self._head:
            self._curr = self._tail if self._curr == None else self._curr._prev
            return self._curr._value
        else:
            raise StopIteration()
    #
    # len
    #
    def __len__(self):
        return self._length

    def __str__(self):
        if self._head == None: return ''
        plst = self._head
        l = []
        while True:
            l.append(plst._value)
            plst = plst._succ
            if plst == None: break
        return ", ".join([str(e) for e in l])
