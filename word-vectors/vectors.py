import matplotlib.pyplot as plt
import numpy as np
import random

import matplotlib
matplotlib.use('TkAgg')

DIMENSIONS = 2
MAX_NUM = 3

f = open("./data/text", "r+")

word_vectors = {}

center = np.array([ MAX_NUM/2 for x in range(DIMENSIONS)])
cont = 0
for line in f.readlines():
    line = line.replace(",","")
    line = line.replace("\n","")
    words = line.split(" ")

    random_array = np.array([ random.uniform(-1,1) for x in range(DIMENSIONS) ])

    for word in words:
        new_vector = word_vectors.get(word, center + random_array)
        word_vectors[word.lower()] = new_vector
    cont += 1
    if False:
        break;

# Plot the data
plt.ylim(0, MAX_NUM)
plt.xlim(0, MAX_NUM)

for k, v in word_vectors.items():
    plt.text(v[0], v[1], k)
    print("Word:",k)
    print("v 0:",v[0])
    print("v 1:",v[1])
plt.show()

print(word_vectors)
