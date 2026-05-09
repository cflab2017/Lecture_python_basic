from collections import Counter
import re

text = """
The quick brown fox jumps over the lazy dog. The dog is sleeping.
The fox runs quickly. Quickly! The fox ran over the dog.
The dog wakes up.
"""

words = re.findall(r"\w+", text.lower())
counter = Counter(words)

print("Top 5:")
for word, count in counter.most_common(5):
    print(f"  {word}: {count}회")
