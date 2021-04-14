import base64
import json
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    print('请安装加解密库pycryptodome')


class AesSample(object):
    def __init__(self):
        self.key = '315ccddc9e04407abf5c3f87c67f506e'.encode('utf-8')
        self.iv = 'www.waitalone.cn'.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encode(self, data):
        cipher = AES.new(self.key, self.mode, self.iv)
        pad_pkcs7 = pad(data.encode('utf-8'), AES.block_size, style='pkcs7')
        result = base64.encodebytes(cipher.encrypt(pad_pkcs7))
        encrypted_text = str(result, encoding='utf-8').replace('\n', '')
        return encrypted_text

    def decode(self, data):
        cipher = AES.new(self.key, self.mode, self.iv)
        base64_decrypted = base64.decodebytes(data.encode('utf-8'))
        una_pkcs7 = unpad(cipher.decrypt(base64_decrypted), AES.block_size, style='pkcs7')
        decrypted_text = str(una_pkcs7, encoding='utf-8')
        return decrypted_text

    def test(self):
        data1 = 'panjie'
        data2 = 's/EdN6CpezFrbCmqDi2VY83KqoU9C/UTVxH1+OBAu6U='
        print('加密结果：', self.encode(data1))
        print('解密结果：', self.decode(data2))


if __name__ == '__main__':
    blog = AesSample()
    blog.test()
    a = json.dumps('{"a":123,"b":222}')
    print(a)