from models.card import PaymentCard
from models.drivers import Driver

from dataclasses import dataclass, field

# Este archivo sera un objeto de estado global
mock_driver = Driver(
    id=1, id_plate="111-III", document_id="22222222", company_ruc="3333333302"
)


@dataclass
class PaymentState:
    driver: Driver = field(init=False)

    def authenticate(self, user: str, password: str):
        # Recuperar
        if user:
            self.driver = Driver(id)

    def pay(self, card: PaymentCard, charge: float):
        if card.id_student:
            charge = 0.75
            # Actualizar el pago

    def _reconnect(self):
        # Manda una señal para recuperar la informacion
        self.driver = mock_driver
