from cryptography.fernet import Fernet

username = "username"
password = 'password'

def encrypt_message(message):
    """
    Encrypts a message
    """
    key =  b'90_bU9VDqBx_GQVVlyIE8BW-qJNiPIXMlcohZsb-XPs='
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message
def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key =  b'90_bU9VDqBx_GQVVlyIE8BW-qJNiPIXMlcohZsb-XPs='
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()
if __name__ == "__main__":
    # enc_pass = encrypt_message(username)
    # print(enc_pass)
    # dec_pass = decrypt_message(enc_pass)
    # print(dec_pass)
    # #--------------------------
    # enc_pass = encrypt_message(password)
    # print(enc_pass)
    # dec_pass = decrypt_message(enc_pass)
    # print(dec_pass)
    pass