import random
import string

caracteres = string.ascii_letters + string.digits
def gerador (tam = 10):
    return ''.join(random.choices(caracteres, k=tam))
print(f"Sugerimos a senha: {gerador(10)}")
