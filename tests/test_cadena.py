import pytest
from src.cadena import invertir_cadena
assert invertir_cadena("Hola") == "aloH"
assert invertir_cadena("Python") == "nohtyP"
assert invertir_cadena("") == ""
assert invertir_cadena("12345") == "54321"
