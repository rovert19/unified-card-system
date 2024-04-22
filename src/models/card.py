from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=False)
class PaymentCard:
    id: int
    id_student: Optional[int] = None
    bank_account: str
    document_id: str
    expiration_date: Optional[float] = None
    last_update: int = 0
    money: float = 0.0
    active: bool = False 
