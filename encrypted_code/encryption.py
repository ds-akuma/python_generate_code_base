# encrypt_code.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_code(file_path, key, output_file):
    # Read the original file content
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Pad the data to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create the cipher object and encrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Write the IV and encrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

if __name__ == "__main__":
    key = os.urandom(32)  # Use a secure method to store this key
    encrypt_code('sample_code_sets/main.py', key, 'encrypted_main.py')
