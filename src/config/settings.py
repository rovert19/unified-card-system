from decouple import config

timestamp_valid = config("TIME_VALID_CARD", cast=int)
db_user = config("DATABASE_USER")
db_password = config("DATABASE_PASSWORD")
