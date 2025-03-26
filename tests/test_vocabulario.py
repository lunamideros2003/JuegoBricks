import pytest
from src.vocabulario import contar_vocales
assert contar_vocales("Hola") == 2
assert contar_vocales("Python") == 1
assert contar_vocales("aeiou") == 5
assert contar_vocales("bcdfg") == 0
