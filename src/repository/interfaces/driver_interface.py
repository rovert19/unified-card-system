from typing import Protocol

from models.driver import Driver


class IDriverRepository(Protocol):
    
    def get_by_id(self, id) -> Driver:
        ...

    
    def create(self, id) -> None:
        ...

    
    def update(self, driver: Driver) -> None:
        ...

    
    def delete(self, driver: Driver) -> int:
        ...


