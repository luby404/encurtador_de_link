import secrets
import string

CHARS = string.digits + string.ascii_letters

def gerar_codigo(tamanho=8):
    return ''.join(secrets.choice(CHARS) for _ in range(tamanho))


