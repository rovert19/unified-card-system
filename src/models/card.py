from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentCard:
    id: int
    id_student: Optional[int] = None
    expiration_date: Optional[float] = None
    last_update: float
    money: float = 0.0
