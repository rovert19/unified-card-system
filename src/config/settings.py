from decouple import config

months_valid = config("MONTHS_VALID_CARD", cast=int)
db_user = config("DATABASE_USER")
db_password = config("DATABASE_PASSWORD")
db_name = config("DATABASE_NAME")
