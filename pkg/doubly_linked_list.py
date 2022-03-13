"""Doubly linked list implementation"""

from typing import Generic, Iterator, MutableSequence, Tuple, TypeVar, Union


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
    index: int

    def __init__(self, node: Node[T], index: int):
        self.node = node
        self.index = index

    def __next__(self) -> T:
        if self.node is None:
            raise StopIteration
        else:
            self.index += 1
            val = self.node.value
            self.node = self.node.next
            return val

    def __prev__(self) -> T:
        if self.node is None:
            raise StopIteration
        else:
            self.index -= 1
            val = self.node.value
            self.node = self.node.prev
            return val

    def __iter__(self) -> "LinkedListIterator[T]":
        return self

    def move_to(self, target_index) -> None:
        """Moves iterator to target index"""
        while self.index < target_index:
            next(self)
        while self.index > target_index:
            self.__prev__()

    @property
    def value(self) -> T:
        """Helper method to hide value implementation"""
        if self.node is None:
            raise StopIteration
        else:
            return self.node.value


class DoublyLinkedList(MutableSequence[T]):
    """
    Doubly linked list implementation of abstract List
    """

    head: Union[Node[T], None]
    tail: Union[Node[T], None]
    size: int

    def __init__(self) -> None:
        super()
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def _get_at_key(self, key: int) -> T:
        node = self._get_node(key)
        return node.value

    def _get_at_slice(self, key: slice) -> "DoublyLinkedList[T]":
        accumulator = DoublyLinkedList()

        iterator = iter(self)
        start, stop, step = key.indices(len(self))
        for index in range(start, stop, step):
            iterator.move_to(index)
            accumulator.append(iterator.value)

        return accumulator

    def _get_at_tuple(
        self, key: Tuple[Union[int, slice], ...]
    ) -> "DoublyLinkedList[T]":
        accumulator = DoublyLinkedList()
        for k in key:
            results = self[k]
            if isinstance(results, DoublyLinkedList):
                accumulator.append(r for r in results)
            else:
                accumulator.append(results)
        return accumulator

    def __getitem__(
        self, key: Union[int, slice, Tuple[Union[int, slice], ...]]
    ) -> Union["DoublyLinkedList[T]", T]:
        if isinstance(key, slice):
            return self._get_at_slice(key)
        elif isinstance(key, Tuple):
            return self._get_at_tuple(key)
        else:
            return self._get_at_key(key)

    def __iter__(self) -> LinkedListIterator[T]:
        if self.head is None:
            raise StopIteration

        return LinkedListIterator(self.head, 0)

    def __str__(self) -> str:
        contents = ", ".join([str(i) for i in self])
        return f"[{contents}]"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MutableSequence):
            return False
        elif len(self) != len(other):
            return False
        else:
            return all([i == j for (i, j) in zip(self, other)])

    def __ne__(self, other: object) -> bool:
        return not self == other

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

    def _add_to_end(self, new_value: T) -> None:
        node = Node(new_value)
        if self.tail:
            self.tail.set_next(node)
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def _set_head_tail(self, new_value) -> None:
        self.head = self.tail = Node(new_value)
        self.size += 1

    def _set_at_index(self, key, new_value):
        old = self._get_node(key)
        node = Node(new_value, old.prev, old.next)
        if node.prev:
            node.prev.next = node
        if node.next:
            node.next.prev = node

    def __setitem__(self, key: int, new_value: T) -> None:
        if key > self.size:
            raise IndexError
        elif key == 0 and len(self) == 0:
            self._set_head_tail(new_value)
        elif key == self.size:
            self._add_to_end(new_value)
        else:
            self._set_at_index(key, new_value)

    def __delitem__(self, key: int) -> None:
        if key >= self.size:
            raise IndexError
        else:
            old = self._get_node(key)
            if old.prev:
                old.prev.next = old.next
            if old.next:
                old.next.prev = old.prev

    def insert(self, index: int, value: T) -> None:
        self[index] = value
