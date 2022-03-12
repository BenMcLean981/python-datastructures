from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


class List(ABC, Generic[T]):
    """
    Abstract base class describing common list methods
    """

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __ne__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __getitem__(self, key: int) -> T:
        pass

    @abstractmethod
    def __setitem__(self, key: int, new_value: T) -> None:
        pass

    @abstractmethod
    def __delitem__(self, key: int) -> None:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        """Add item to list"""
