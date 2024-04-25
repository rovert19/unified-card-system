from dataclasses import dataclass
import uuid

# transport company tiene campos como company_ruc, company_name, company_propietario
# automatizar la creacion de las tablas y database


@dataclass(frozen=True)
class Driver:
    id: uuid.UUID
    user: str
    password: str
    id_plate: str
    bank_account: str
