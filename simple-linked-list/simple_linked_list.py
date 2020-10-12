class Node:
    def __init__(self, value):
        self._value = value
        self._succ = None

    def value(self):
        return self._value

    def next(self):
        return self._succ


class EmptyListException(Exception):
    pass


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._curr = None
        self._rcurr = None
        self._length = 0
        if values != None and len(values) > 0:
            for elem in values:
                self.push(elem)

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def head(self):
        if self._head == None or self.is_empty():
            raise EmptyListException("Empty list!")
        return self._head

    def push(self, value):
        node = Node(value)
        node._succ = self._head
        self._head = node
        self._length += 1
        self

    def pop(self):
        if self._head == None or self.is_empty():
            raise EmptyListException("Empty list!")
        node = self._head
        self._head = self._head._succ
        self._length -= 1
        if self._length == 0: self._head = None
        node._succ = None
        return node._value

    def __iter__(self):
        self._curr = self._head
        self._rcurr = self._length
        return self

    def __next__(self):
        """
        'natural' order from head to 'tail'
        """
        if self.is_empty(): raise StopIteration()

        if self._curr != None:
            value = self._curr._value
            self._curr =  self._curr._succ
            return value
        else:
            raise StopIteration()

    def __reversed__(self):
        if self.is_empty(): raise StopIteration()

        if self._rcurr != 0:
            ptr, ix = self._head, 1
            while ix < self._rcurr:
                ix += 1
                ptr = ptr._succ
            self._rcurr -= 1
            return ptr._value
        else:
            raise StopIteration()

    def reversed(self):
        return list(self)[::-1]

    def __str__(self):
        if self._head == None: return ''
        plst = self._head
        l = []
        while True:
            l.append(plst._value)
            plst = plst._succ
            if plst == None: break
        return ", ".join([str(e) for e in l])
