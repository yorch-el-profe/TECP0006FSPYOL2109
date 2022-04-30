import time
from fibonacci import *

start_time = time.time() # Toma el tiempo inicial

fibonacci(100)

end_time = time.time() # Toma el tiempo final

print("El algoritmo tardo {} segundos".format((end_time - start_time)))