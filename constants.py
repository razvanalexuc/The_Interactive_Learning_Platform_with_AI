from typing import Final
from os import environ
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACEHUB_API_TOKEN: Final[str] = environ["HUGGINGFACEHUB_API_TOKEN"]
COURIER_AUTH_TOKEN: Final[str] = environ["COURIER_AUTH_TOKEN"]

# Verifică dacă variabilele sunt încărcate corect
if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN nu este setat în OS")
if not COURIER_AUTH_TOKEN:
    raise ValueError("COURIER_AUTH_TOKEN nu este setat în OS")