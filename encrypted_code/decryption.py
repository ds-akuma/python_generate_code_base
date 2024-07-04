# decrypt_code.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def decrypt_code(encrypted_file, key, output_file):
    # Read the encrypted file content
    with open(encrypted_file, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()
    
    # Create the cipher object and decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Unpad the data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    key = b'your-32-byte-key-here'  # Use the same key that was used for encryption
    decrypt_code('encrypted_main.py', key, 'decrypted_main.py')
