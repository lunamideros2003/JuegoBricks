import pytest
from temperatura import celsius_a_fahrenheit,fahrenheit_a_celsius,celsius_a_fahrenheit,fahrenheit_a_celsius
assert celsius_a_fahrenheit(0) == 32
assert fahrenheit_a_celsius(32) == 0
assert celsius_a_fahrenheit(100) == 212
assert fahrenheit_a_celsius(212) == 100
