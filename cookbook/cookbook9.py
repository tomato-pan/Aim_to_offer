# 序列中出现次数最多的元素
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_two = word_counts.most_common(2)
print(word_counts["look"])  # 实际上是一个可哈希的元素---字典k-次数
print(top_two)

# Counter可以计算---如果常见需要制表或者计数 可优先使用
import hmac, base64, struct, hashlib, time

def get_hotp_token(secret, intervals_no):
    key = base64.b64decode(secret)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

if __name__ == '__main__':
    secret_key = "arablowt3tycc2oo2irf2lpokhy5vosm"
    print(get_hotp_token(secret_key,int(time.time())//30))