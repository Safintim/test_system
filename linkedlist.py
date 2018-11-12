class Node:
    def __init__(self, v):
        self.__value = v
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, n):
        self.__next = n


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.current = self.head
        else:
            self.tail.set_next(item)
        self.tail = item

    def print_all_nodes(self):
        node = self.head

        while node is not None:
            print(node.get_value())
            node = node.get_next()

    def find(self, val):
        node = self.head

        while node is not None:
            if node.get_value() == val:
                return node
            node = node.get_next()
        return None

    def find_all(self, val):
        node = self.head
        result_list = []

        while node is not None:
            if node.get_value() == val:
                result_list.append(node)
            node = node.get_next()

        return result_list

    def delete(self, v, all=False):
        node = self.head
        prev = node

        while node is not None:
            if self.head.get_value() == v:
                self.head = self.head.get_next()
                if not all:
                    break
            elif node.get_value() == v:
                prev.set_next(node.get_next())
                if not all:
                    break
                node = prev

            prev = node
            node = node.get_next()

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

    def insert(self, afterNode, newNode):
        node = self.head

        while node is not None:
            if node == afterNode:
                newNode.set_next(node.get_next())
                node.set_next(newNode)
                break
            node = node.get_next()

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr
