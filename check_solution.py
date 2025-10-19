from cryptography.fernet import Fernet
from pickle import Unpickler
import ast


def main():
    # Read key from file and remove whitespace
    with open('answer.txt', 'r', encoding='utf-8') as f:
        key = ast.literal_eval(''.join(f.read().split()))

    if not key:
        print("Error: Key is empty")
        return

    token = ()
    with open('secret', 'rb') as f:
        pick = Unpickler(f)
        token = pick.load()

    f = Fernet(key)
    text = f.decrypt(token)
    print(text)


if __name__ == "__main__":
    main()
