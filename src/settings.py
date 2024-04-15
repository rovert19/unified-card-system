from decouple import config

timestamp_valid = config("TIME_VALID_CARD", cast=int)
