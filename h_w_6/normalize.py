import os
import re
import sys
from pathlib import Path

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")


TRANS = {}

# cтворємо ключі і значення
for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    # для маленьких
    TRANS[ord(key)] = value 
    # для великих
    TRANS[ord(key.upper())] = value.upper()


def normalize(name):
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', "_", new_name)
    return f"{new_name}.{'.'.join(extension)}"


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")
    arg = Path(path)
    normalize(path)
