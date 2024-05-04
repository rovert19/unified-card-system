from sqlalchemy import create_engine, URL
from sqlalchemy.sql import text
from src.config import settings


DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host="localhost", 
    port=5432,
    database=settings.db_name    
)

engine = create_engine(DATABASE_URL)
db = engine.connect()

statement_select = text(
    """
        SELECT *
        FROM card
        WHERE id = :id;
    """)

statement_insert = text(
    """
        INSERT INTO card(id, id_student, document_id, expirate, balance)
        VALUES (:id, :id_student, :document_id, :expirate, :balance)
    """)

statement_update_balance = text(
    """
        UPDATE card
        SET balance = :balance
        WHERE id = :id
    """
)

statement_delete = text(
    """
        DELETE FROM card
        WHERE id = :id
    """
)