from pprint import pprint


list_ = [{'dec': value,
          'bin': bin(value),
          'oct': oct(value),
          'hex': hex(value)
          } for value in range(16)]  # до 15 включительно

pprint(list_)
