from typing import Protocol, Optional

from models.card import PaymentCard


class ICardRepository(Protocol):
    
    async def get_by_id(self, id) -> Optional[PaymentCard]:
        ...

    
    async def create(self, paymentCard: PaymentCard) -> None:
        ...

    
    async def update(self, paymentCard: PaymentCard) -> None:
        ...

    
    def delete(self, paymentCard: PaymentCard) -> int:
        ...
