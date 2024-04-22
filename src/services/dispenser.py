from config import settings
from models.card import PaymentCard

import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol, Optional


class Dispenser(Protocol):
    async def registry_card(self, id_student: Optional[int], document_id: str) -> None:
        ...

    async def recharge(self, id: int, charge: float) -> None:
        ...

    def update_card(self) -> PaymentCard:
        ...

    async def get_card(
        self, init_charge: float
    ) -> PaymentCard:
        ...


@dataclass
class DispenserMachine:
    payment_card: PaymentCard = field(init=False)

    async def registry_card(self, id_student: Optional[int], document_id: str):
        id_ = int(datetime.now().timestamp() * 100000)
        has_cards_document_id = [] # recuperar de una base de datos
        
        if not has_cards_document_id:
            is_adult = True
            # comprobar si el DNI es de un menor de edad
            # crear una cuenta bancaria relacionado al DNI
            if is_adult:
                bank_account = "00-0001-001111"
            else:
                bank_account = "12-1001-001111"
        else:
            # recuperar la cuenta bancaria al DNI
            bank_account = "00-0001-001111"
        
        if not id_student:
            self.payment_card = PaymentCard(
                id_,bank_account, document_id, last_update=id_, active=True
            )
        # guardar en la base de datos
        asyncio.sleep(200)
        print(f"Se agrego la tarjeta {self.payment_card}")
        return id_
    
    
    async def recharge(self, id: int, charge: float = 0.0) -> None:
        # get card by id
        self.payment_card.money += charge
        asyncio.sleep(500)
        # actualizar el monto a la BBDD
        return { "message": "Se cargo correctamente el monto a la tarjeta" }


    def update_card(self):
        try:
            self.payment_card
        except:
            print("No existe un payment card cacheado a la maquina")

    
    async def get_card(
        self, init_charge: float = 0.0
    ) -> PaymentCard:
        
        try:
            id_card = await self.registry_card()
            await self.recharge(id_card, init_charge)
            return { 'dispense': True }
        except:
            print("No se configuro ninguna card")
            return { 'dispense': False }


@dataclass
class DispenserPerson:
    payment_card: PaymentCard = field(init=False)

    async def registry_card(self, id_student: Optional[int], document_id: str):
        time_create = datetime.now().timestamp()
        expiration_date = None
        id_ = int(time_create * 100000)
        
        has_cards_document_id = [] # recuperar de una base de datos
        
        if not has_cards_document_id:
            is_adult = True
            # comprobar si el DNI es de un menor de edad
            # crear una cuenta bancaria relacionado al DNI
            if is_adult:
                bank_account = "00-0001-001111"
            else:
                bank_account = "12-1001-001111"
        else:
            # recuperar la cuenta bancaria al DNI
            bank_account = "00-0001-001111"

        if id_student:
            expiration_date = int((time_create + settings.timestamp_valid) * 100000)

        self.payment_card = PaymentCard(
            id_, id_student, bank_account, document_id, expiration_date, last_update=id_, active=True
        )

        asyncio.sleep(200)
        print(f"Se agrego la tarjeta {self.payment_card}")
        # guardar en la BBDD

    async def recharge(self, id: int, charge: float = 0.0) -> None:
        try:
            # get card by id
            self.payment_card.money += charge
            asyncio.sleep(500)
            # actualizar el monto a la BBDD
            return { "message": "Se cargo correctamente el monto a la tarjeta" }
        except:
            return { "message": "Fallo del sistema, no se pudo cargar el metodo" }


    def update_card(self):
        try:
            self.payment_card
        except:
            print("No existe un payment card cacheado a la maquina")

    async def get_card(
        self, id_student: Optional[int], document_id: str, init_charge: float = 0.0
    ) -> PaymentCard:
        try:
            id_card = await self.registry_card(id_student, document_id)
            await self.recharge(id_card, init_charge)
            return { 'dispense': True }
        except:
            print("No se configuro ninguna card")
            return { 'dispense': False }
