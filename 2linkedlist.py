class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, n):
        self.next = n

    def set_prev(self, n):
        self.prev = n


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, v):
        node = self.head

        while node is not None:
            if node.get_value() == v:
                return node
            node = node.get_next()
        return None

    def delete(self, v):
        node = self.find(v)
        if self.head.get_value() == v:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif self.tail.get_value() == v:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            if node is not None:
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
            else:
                return None
        return None

    def clean(self):
        self.head = None
        self.tail = None

        return None

    def len(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.get_next()
        return length

    def insert(self, prev, current):
        node_start = self.head

        while node_start is not None:
            if node_start == prev:
                current.set_next(node_start.get_next())
                current.set_prev(node_start)
                node_start.set_next(current)
                node_start.get_next().set_prev(current)

            node_start = node_start.get_next()

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.head.set_prev(item)
            item.set_next(self.head)
            self.head = item
            self.head.set_prev(None)
