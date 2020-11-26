import string
import random
strings = list(string.ascii_letters)
for x in range(0,10):
    strings.append(str(x))

x=''.join(random.sample(strings,4))
print(x)