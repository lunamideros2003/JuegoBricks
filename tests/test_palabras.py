import pytest
from src.palabras import contar_palabras
assert contar_palabras("Hola mundo") == 2
assert contar_palabras("Python es un lenguaje poderoso") == 5
assert contar_palabras("   Esto   tiene   espacios   extras   ") == 4
assert contar_palabras("") == 0
assert contar_palabras("123 456 789") == 3
