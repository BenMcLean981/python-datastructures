"""Collection of tests for DoublyLinkedList"""
import pytest
from pkg.doubly_linked_list import DoublyLinkedList


def make_example_list() -> DoublyLinkedList[int]:
    """
    Helper to setup doublyLinkedList
    """
    my_list = DoublyLinkedList()
    my_list.append(5)
    my_list.append(3)
    my_list.append(2)

    return my_list


def test_init():
    """
    Test initialization of DoublyLinkedList
    """
    my_list = DoublyLinkedList()
    assert my_list.head is None
    assert my_list.tail is None
    assert my_list.size is 0


def test_append():
    """Test addition of members to list"""
    my_list = DoublyLinkedList()

    my_list.append(5)
    assert my_list.size is 1

    my_list.append(3)
    assert my_list.size is 2

    my_list.append(2)
    assert my_list.size is 3


def test__getitem__():
    """Test list get by index"""
    my_list = make_example_list()
    assert my_list[0] == 5
    assert my_list[1] == 3
    assert my_list[2] == 2
    assert my_list[-1] == 2
    assert my_list[-2] == 3
    assert my_list[-3] == 5

    with pytest.raises(IndexError):
        _ = my_list[3]


def test__getitem__slice():
    """Test list get by slice"""
    my_list = make_example_list()
    assert my_list[0:] == my_list
    assert my_list[0:3] == my_list
    assert my_list[1:] == [3, 2]
    assert my_list[1:2] == [3]
    assert my_list[:-1] == [5, 3]


def test__getitem__tuple():
    """Test list get by tuple"""
    my_list = make_example_list()
    assert my_list[0, 1] == [5, 3]
    assert my_list[1, 2] == [3, 2]
    assert my_list[-1, 2] == [2, 2]


def test__setitem__():
    """Test list set by index"""
    my_list = make_example_list()

    my_list[3] = 5
    assert my_list[3] == 5

    my_list[1] = 0
    assert my_list[1] == 0

    assert my_list == [5, 0, 2, 5]


def test__str():
    """Test converting list to str"""
    my_list = make_example_list()
    assert my_list.__str__() == "[5, 3, 2]"
    assert str(my_list) == "[5, 3, 2]"


def test__repr__():
    """Test repr of list"""
    my_list = make_example_list()
    assert my_list.__repr__() == "[5, 3, 2]"
    assert repr(my_list) == "[5, 3, 2]"


def test__iter__():
    """Test doubly linked list iteration"""
    my_list = make_example_list()
    my_iter = iter(my_list)
    assert next(my_iter) == 5
    assert next(my_iter) == 3
    assert next(my_iter) == 2

    with pytest.raises(StopIteration):
        next(my_iter)


def test__eq__():
    """Test whether lists are equal"""
    my_list_1 = make_example_list()
    my_list_2 = make_example_list()

    assert my_list_1 == my_list_2
    my_list_2.append(5)
    assert my_list_1 != my_list_2
    my_list_1.append(4)
    assert my_list_1 != my_list_2

    assert my_list_1 == [5, 3, 2, 4]
