from string import ascii_lowercase, ascii_uppercase, digits
from random import sample


def get_random_password(length: int = 8) -> str:
    random_str = ascii_lowercase + ascii_uppercase + digits
    password = ''.join(sample(random_str, length))
    return password


print(get_random_password())
