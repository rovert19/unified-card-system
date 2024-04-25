from dataclasses import dataclass
from typing import Optional
import uuid
from datetime import datetime, _Date


@dataclass(frozen=False)
class PaymentCard:
    id: uuid.UUID
    id_student: Optional[str]
    bank_account: str
    expiration_date: Optional[_Date]
    active: bool = False
