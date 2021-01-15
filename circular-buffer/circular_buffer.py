class BufferFullException(BaseException):
    pass


class BufferEmptyException(BaseException):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        assert capacity > 0, f"expecting capacity to be > 0"

        self.cap = capacity
        self.nfill = 0
        self.buf = [[] for _ in range(capacity)]
        self.head = self.tail = -1

    def read(self):
        if self.nfill == 0:
            raise BufferEmptyException("Empty buffer")

        item = self.buf[self.head]
        self.head = (self.head + 1) % self.cap
        self.nfill -= 1
        return item

    def write(self, data):
        if self.nfill == self.cap:
            raise BufferFullException("Full buffer")
        #
        self.tail = (self.tail + 1) % self.cap

        if self.nfill == 0:            # buf was empty, first write
            self.head = self.tail

        self.nfill += 1
        self.buf[self.tail] = data
        return self

    def overwrite(self, data):
        self.tail = (self.tail + 1) % self.cap

        if self.head == self.tail:
            self.head = (self.head + 1) % self.cap

        if self.nfill < self.cap:      # then, we need to incr. nfill
            self.nfill += 1

        self.buf[self.tail] = data
        return self

    def clear(self):
        self.nfill = 0
        self.head = self.tail = -1
