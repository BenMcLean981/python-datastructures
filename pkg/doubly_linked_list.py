"""Doubly linked list implementation"""

from typing import Generic, Iterator, TypeVar, Union
from .list import List


T = TypeVar("T")


class Node(Generic[T]):
    """Node of a doubly linked list"""

    value: T
    prev: Union["Node[T]", None]
    next: Union["Node[T]", None]

    def __init__(
        self,
        value: object = None,
        prev: Union["Node[T]", None] = None,
        next_node: Union["Node[T]", None] = None,
    ):
        self.value = value
        self.prev = prev
        self.next = next_node

    def has_next(self) -> bool:
        """Check if next is defined"""
        return self.next is not None

    def set_next(self, node: "Node[T]") -> None:
        """Set next to node"""
        self.next = node


class LinkedListIterator(Iterator[T]):
    """
    Iterator for doubly linked list

    Goes in order of list elements
    """

    node: Union[Node[T], None]

    def __init__(self, node: Node[T]):
        self.node = node

    def __next__(self) -> T:
        if self.node is None:
            raise StopIteration
        else:
            val = self.node.value
            self.node = self.node.next
            return val

    def __iter__(self) -> "LinkedListIterator[T]":
        return self

    @property
    def value(self) -> T:
        """Helper method to hide value implementation"""
        if self.node is None:
            raise StopIteration
        else:
            return self.node.value


class DoublyLinkedList(List[T]):
    """
    Doubly linked list implementation of abstract List
    """

    head: Union[Node[T], None]
    tail: Union[Node[T], None]

    def __init__(self) -> None:
        super()
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

    def __getitem__(self, key: int) -> T:
        node = self._get_node(key)
        return node.value

    def __iter__(self) -> LinkedListIterator[T]:
        if self.head is None:
            raise StopIteration

        return LinkedListIterator(self.head)

    def __str__(self) -> str:
        contents = ", ".join([str(i) for i in self])
        return f"[{contents}]"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, List):
            return False
        elif len(self) != len(other):
            return False
        else:
            return any([i != j for (i, j) in zip(self, other)])

    def __ne__(self, other: object) -> bool:
        return self != other

    def _get_node(self, key: int) -> Node[T]:
        if key >= self.size:
            raise IndexError
        list_iter = iter(self)

        num_iters = key if key >= 0 else self.size + key

        for _ in range(num_iters):
            next(list_iter)
        if list_iter.node is None:
            # This is unreachable, but for linting
            # We need it
            raise IndexError
        return list_iter.node

    def __setitem__(self, key: int, new_value: T) -> None:
        if key >= self.size:
            raise IndexError
        else:
            old = self._get_node(key)
            # another option would be to replace old.value
            # with new_value, but someone else could be using
            # old and then they would see value change
            # unexpectedly
            node = Node(new_value, old.prev, old.next)
            if node.prev:
                node.prev.next = node
            if node.next:
                node.next.prev = node

    def __delitem__(self, key: int) -> None:
        if key >= self.size:
            raise IndexError
        else:
            old = self._get_node(key)
            if old.prev:
                old.prev.next = old.next
            if old.next:
                old.next.prev = old.prev
