from fileinput import filename

from app.decrypt import Decryptor
from app.encrypt import Encryptor
import os


# import io

class FileAdapter:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self) -> bytes:
        try:
            name = str(self.filename)
            fileName = os.path.join("..", "data", name)
            with open(fileName, 'rb') as file:

                content = file.read()
                print(content)
            return bytes(content)

        except FileNotFoundError:
            print(f"File not found: {self.filename}")


def main():
    enc = Encryptor("plaintext_key")
    dec = Decryptor("plaintext_key")

    name = "frame.png"
    # file = FileAdapter(name).read_data()    #invalid type
    file = FileAdapter(name)

    encrypted_file = enc.encrypt(file)
    print("")
    print("file: frame.png (encrypted)")
    # print("encrypt: ", encrypted_file)

    decrypted_file = dec.decrypt(encrypted_file)
    print("")
    print("file: frame.png (decrypted)")
    # print("dencrypt: ", decrypted_file)

    # decrypted_file = dec.decrypt(file)         #ERROR occurs for InvalidToken
    # print("")
    # print("dencrypt2: ", decrypted_file)

    # Write bytes to a new file  # not necessary
    with open("../data/new_image.png", "wb") as new_file:
        new_file.write(decrypted_file)


if __name__ == "__main__":
    main()
