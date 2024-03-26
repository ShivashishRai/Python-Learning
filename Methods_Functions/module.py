
from collections import Counter

string_frequency = " The Sting is so Right"
freq = Counter(string_frequency)
print(freq)
print(freq.most_common(1))

