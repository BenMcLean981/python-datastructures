"""Doubly linked list implementation"""

from typing import Union
from .list import List


class Node:
    """Node of a doubly linked list"""

    value: Union[object, None]
    prev: Union["Node", None]
    next: Union["Node", None]

    def __init__(
        self, value: object = None, prev: "Node" = None, next_node: "Node" = None
    ):
        self.value = value
        self.prev = prev
        self.next = next_node

    def has_next(self) -> bool:
        """Check if next is defined"""
        return self.next is not None

    def set_next(self, node: "Node") -> None:
        """Set next to node"""
        self.next = node


class LinkedListIterator:
    """
    Iterator for doubly linked list

    Goes in order of list elements
    """

    node: Union[Node, None]

    def __init__(self, node: Node):
        self.node = node

    def __next__(self) -> object:
        if self.node is None:
            raise StopIteration
        else:
            v = self.node.value
            self.node = self.node.next
            return v

    def __iter__(self) -> "LinkedListIterator":
        return self


class DoublyLinkedList(List):
    """
    Doubly linked list implementation of abstract List
    """

    head: Union[Node, None]
    tail: Union[Node, None]

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, item: object) -> None:
        node = Node(item, self.tail)

        if self.tail:
            self.tail.set_next(node)
            self.tail = self.tail.next
        else:
            self.head = self.tail = node

        self.size += 1

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, key: int) -> object:
        if key >= self.size:
            raise IndexError("Index out of range")
        i = iter(self)
        for _ in range(key):
            i = next(i)
        return i.value

    def __iter__(self) -> "Node":
        if self.head is None:
            raise StopIteration

        return LinkedListIterator(self.head)

    def __str__(self) -> str:
        contents = ", ".join([str(i) for i in self])
        return f"[{contents}]"

    def __repr__(self) -> str:
        return str(self)
