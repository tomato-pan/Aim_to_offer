import json

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

class RsaDemo():
    def _rsa_decrypt(priv_key_str, msg):
        """
        静态方法，根据私钥解密字符串
        :param priv_key_str: 私钥完整
        :param msg: 公钥加密字符串
        :return:
        """
        msg = base64.b64decode(msg)
        length = len(msg)
        default_length = 128
        # 私钥解密
        priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(priv_key_str))
        # 长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(msg, b' '))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(msg[offset:offset + default_length], b' '))
            else:
                res.append(priobj.decrypt(msg[offset:], b' '))
            offset += default_length

        return b''.join(res)

    def _rsa_encrypt(pub_key_str, msg):
        """
        静态方法,根据公钥加密字符串
        :param pub_key_str: 公钥完整
        :param msg: 待加密json文本
        :return:
        """
        msg = msg.encode('utf-8')
        length = len(msg)
        default_length = 117
        # default_length = 100
        # 公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(pub_key_str))
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)

        return base64.b64encode(byte_data)

    def rsa_decrypt(self, msg):
        """
        解密文本到b’二进制值
        :param msg:
        :return:
        """
        return self._rsa_decrypt(self.get_private_key(), msg)

    def rsa_decrypt2str(self, msg):
        """
        获取解密文本
        :param msg: 加密后的文本
        :return:
        """
        return self.rsa_decrypt(msg).decode("utf-8")  # 解密成byte并转为utf-8字符串

    def rsa_decrypt2dict(self, msg):
        """
        获取解密json文本到dict
        :param msg: 加密后的文本
        :return:
        """
        return json.loads(self.rsa_decrypt2str(msg))  # 得到传输过来的数据的dict

    def rsa_encrypt(self, msg, pub_key=None):
        """
        加密一段字符串变成 b'二进制
        :param msg: 待加密文本
        :param pub_key: 公钥，不填默认获取初始化的
        :return:
        """
        pub_key = pub_key or self.get_public_key()
        return self._rsa_encrypt(pub_key, msg)

    def rsa_encrypt2str(self, msg):
        """
        加密文本到文本
        :param msg: 待加密文本
        :return:
        """
        return self.rsa_encrypt(msg).decode("utf-8")  # 加密成待传输的字符串

