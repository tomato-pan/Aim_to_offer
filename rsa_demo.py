from Crypto.PublicKey import RSA
import Crypto.Cipher.PKCS1_v1_5 as cipher


def generate_key(bits):
    '''
    :param bits: the length of RSA key
    :return: RSAKey object
    '''


    return RSA.generate(bits)


def encrypt(message, pk):
    '''
    :param message: the message would be encrypted
    :param pk: the public key
    :return: a cipher text for the message though encrypt
    :rtype: bytes
    '''


    cipher_obj = cipher.new(RSA.importKey(pk))
    org_bytes = message.encode()
    length_en = RSA.RsaKey.size_in_bytes(RSA.importKey(pk)) - 11  # 2048/8-11=245

    res_en = b''
    for i in range(0, len(org_bytes), length_en):
        res_en += cipher_obj.encrypt(org_bytes[i: i + length_en])
    cipher_text = res_en
    return cipher_text


def decrypt(cipher_text, sk):
    '''
    :param message: the cipher text would be decrypted
    :param pk: the private key
    :return: a message for the cipher text though decrypt
    :rtype: string
    '''


    cipher_obj = cipher.new(RSA.importKey(sk))
    length_de = RSA.RsaKey.size_in_bytes(RSA.importKey(sk))

    res_de = b''
    for i in range(0, len(cipher_text), length_de):
        res_de += cipher_obj.decrypt(cipher_text[i:i + length_de], 'DecryptError')  # for pkcs
    plaint_text = res_de.decode()
    return plaint_text

if __name__ == "__main__":
    key = generate_key(2048)  # 2048 is the length of RSA key
    pk = key.publickey().export_key()  # for public key
    sk = key.export_key()  # for private key

    message = "We are different, work hard!" * 20
    cipher_text = encrypt(message, pk)
    print(cipher_text)
    print(type(cipher_text))
    plaint_text = decrypt(cipher_text, sk)
    print(plaint_text)
    print(message == plaint_text)
