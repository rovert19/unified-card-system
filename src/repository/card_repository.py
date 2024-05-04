
from dataclasses import asdict
from typing import Any, Optional
import uuid

from models.card import PaymentCard
from repository.interfaces.card_interface import ICardRepository

from db.connect import db
from db.connect import statement_select, statement_insert, statement_update_balance


class SQLCardRepository(ICardRepository):
    async def get_by_id(self, card_id: uuid.UUID) -> Optional[PaymentCard]:
        try:
            with db.begin():
                result = db.execute(statement_select, {"id": card_id})
                card_tuple = result.fetchmany(1)[0]
                if not card_tuple:
                    raise ValueError("Not exist the card")
            
            return PaymentCard(*card_tuple)
        except:
            return None
    
    async def create(self, paymentCard: PaymentCard) -> None:
        try:
            with db.begin():
               db.execute(statement_insert, asdict(paymentCard))

            return {
                "message": "Added card in database"
            }
        except:
            return {
                "error": "Fail database"
            }

    async def update(self, card_id: uuid.UUID, bus_fare: float = None) -> None:
        try:
            with db.begin():
                result = db.execute(statement_select, {"id": card_id})
                card_tuple = result.fetchmany(1)[0]
                paymentCard = PaymentCard(*card_tuple)
                
                if bus_fare > paymentCard.balance:
                    raise ValueError("Saldo insuficiente")
                
                new_balance = paymentCard.balance - bus_fare
                
                card_info_update = {
                    "id": paymentCard.id,
                    "balance": new_balance
                }
                db.execute(statement_update_balance, **card_info_update)
                return {
                    "message": "Ticket paid"
                }

        except:
            return {
                "error": "Saldo insuficiente"
            }

    
    def delete(self, card_id: uuid.UUID) -> dict[str, Any]:
        try:
            with db.begin():
                db.execute(statement_insert, {"id": card_id})
                return {
                    'id': card_id,
                    'message': 'Delete the payment card'
                }
        except:
            return None
        