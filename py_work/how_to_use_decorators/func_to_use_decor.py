#func to use Decorator

from decor import document_it
from square import square_it

@square_it
@document_it

def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
