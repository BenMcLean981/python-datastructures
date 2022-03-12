import pytest
from pkg.doubly_linked_list import DoublyLinkedList


def make_example_list() -> DoublyLinkedList[int]:
    """
    Helper to setup doublyLinkedList
    """
    my_list = DoublyLinkedList()
    my_list.add(5)
    my_list.add(3)
    my_list.add(2)

    return my_list


def test_init():
    """
    Test initialization of DoublyLinkedList
    """
    my_list = DoublyLinkedList()
    assert my_list.head is None
    assert my_list.tail is None
    assert my_list.size is 0


def test_add():
    """Test addition of members to list"""
    my_list = DoublyLinkedList()

    my_list.add(5)
    assert my_list.size is 1

    my_list.add(3)
    assert my_list.size is 2

    my_list.add(2)
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
    l = make_example_list()
    i = iter(l)
    assert next(i) == 5
    assert next(i) == 3
    assert next(i) == 2

    with pytest.raises(StopIteration):
        next(i)
