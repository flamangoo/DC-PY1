from string import ascii_lowercase, ascii_uppercase, digits
from random import sample


def get_random_password(n: int = 8) -> str:
    selection_str = ascii_lowercase + ascii_uppercase + digits
    password = ''.join(sample(selection_str, n))
    return password


print(get_random_password())
