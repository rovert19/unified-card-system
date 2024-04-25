from abc import ABC, abstractmethod

from models.driver import Driver


class DriverRepository(ABC):
    @abstractmethod
    def get_by_id(self, id) -> Driver:
        pass

    @abstractmethod
    def create(self, id) -> None:
        pass

    @abstractmethod
    def update(self, driver: Driver) -> None:
        pass

    @abstractmethod
    def delete(self, driver: Driver) -> int:
        pass


class SQLDriverRepository(DriverRepository):
    pass
