from abc import ABC, abstractmethod

from models.card import PaymentCard


class CardRepository(ABC):
    @abstractmethod
    def get_by_id(self, id) -> PaymentCard:
        pass

    @abstractmethod
    def create(self, id) -> None:
        pass

    @abstractmethod
    def update(self, paymentCard: PaymentCard) -> None:
        pass

    @abstractmethod
    def delete(self, paymentCard: PaymentCard) -> int:
        pass


class SQLCardRepository(CardRepository):
    pass
