from fibonacci_error import FibonacciError
from memoize import *

@memoize
def fibonacci(n):
  if n == 1 or n == 2:
    return 1

  if n <= 0:
    # Lanzar un error (o excepción indicando el problema)
    raise FibonacciError
  
  return fibonacci(n - 1) + fibonacci(n - 2)