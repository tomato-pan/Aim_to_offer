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
