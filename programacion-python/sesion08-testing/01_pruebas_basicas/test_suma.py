from suma import suma
import pytest

def test_cero():
  resultado = suma(0, 0)
  # Verificar que resultado sea 0
  assert resultado == 0


def test_positivos():
  resultado1 = suma(10, 20)
  resultado2 = suma(100, 1000)
  resultado3 = suma(111, 222)

  assert resultado1 == 30
  assert resultado2 == 1100
  assert resultado3 == 333

def test_numeros_cadenas():
  resultado = suma("1", "2")
  assert resultado == 3

def test_cadenas():
  with pytest.raises(ValueError):
    resultado = suma("a", "b")