

import sys
from Potatoizer import Potatoizer


if __name__ == '__main__':
    if len(sys.argv) == 2:
        Potatoizer(sys.argv[1]).potatoize()
    else:
        print("Usage: python3 Potatoize.py <file_path>")
