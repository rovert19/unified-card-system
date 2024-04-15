from dataclasses import dataclass, field
from ..settings import timestamp_valid
from datetime import datetime, timedelta
from typing import Protocol, Optional
from models import PaymentCard


class Dispenser(Protocol):
    def registry_card(self) -> None:
        ...

    def get_card(self, id_student: Optional[int], init_charge: float) -> PaymentCard:
        ...


@dataclass
class DispenserMachine:
    payment_card: PaymentCard = field(init=False)

    def _registry_card(self):
        print("Se agrego la tarjeta {self.payment_card}")

    def get_card(
        self, id_student: Optional[int], init_charge: float = 0.0
    ) -> PaymentCard:
        id_ = int(datetime.now().timestamp() * 100000)
        if not id_student:
            self.payment_card = PaymentCard(id=id_, last_update=id_, money=init_charge)
        self._registry_card()
        return self.payment_card


@dataclass
class DispenserPerson:
    payment_card: PaymentCard = field(init=False)

    def _registry_card(self):
        print("Se agrego la tarjeta {self.payment_card}")

    def get_card(
        self, id_student: Optional[int], init_charge: float = 0.0
    ) -> PaymentCard:
        time_create = datetime.now().timestamp()
        id_ = int(time_create * 100000)
        if id_student:
            expiration_date = int((time_create + timestamp_valid) * 100000)
            self.payment_card = PaymentCard(
                id_, id_student, expiration_date, last_update=id_, money=init_charge
            )
        else:
            self.payment_card = PaymentCard(id_, last_update=id_, money=init_charge)
        self._registry_card()
        return self.payment_card
