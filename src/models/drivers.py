from dataclasses import dataclass


# transport company tiene campos como company_ruc, company_name, company_propietario
# automatizar la creacion de las tablas y database


@dataclass(frozen=True)
class Driver:
    id: int
    user: str
    password: str
    id_plate: str
    document_id: str
    company_ruc: int
