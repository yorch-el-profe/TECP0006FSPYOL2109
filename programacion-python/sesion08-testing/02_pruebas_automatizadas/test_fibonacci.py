# 1 1 2 3 5 8 13 21 34 55 ...
from fibonacci import *
import pytest

@pytest.mark.parametrize('n', [
  1, 2
])
def test_caso_base(n):
  resultado = fibonacci(n)
  assert resultado == 1

@pytest.mark.parametrize('n, resultado_esperado', [
  (3, 2),   # Verifica que: fibonacci(3) = 2
  (6, 8),   # Verifica que: fibonacci(6) = 8
  (10, 55), # Verifica que: fibonacci(10) = 55
  (9, 34),  # Verifica que: fibonacci(9) = 34
  (8, 21)   # Verifica que: fibonacci(8) = 21
])
def test_casos_particulares(n, resultado_esperado):
  resultado = fibonacci(n)
  assert resultado == resultado_esperado

@pytest.mark.parametrize('n', [
  -10, -1000, -1, -1.5, -322143283
])
def test_negativos(n):
  with pytest.raises(FibonacciError):
    resultado = fibonacci(n)