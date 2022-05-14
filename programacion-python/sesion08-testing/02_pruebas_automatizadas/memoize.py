def memoize(fibonacci):
  memoria = {}

  def fibonacci_optimizado(n):
    if n not in memoria:
      memoria[n] = fibonacci(n)
    return memoria[n]

  return fibonacci_optimizado