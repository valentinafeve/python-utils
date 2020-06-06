import matplotlib.pyplot as plt
import numpy as np
import random

import matplotlib
matplotlib.use('TkAgg')

DIMENSIONS = 2
LIMIT = 20
NEW_RATIO = 2

f = open("./data/text", "r+")

word_vectors = {}

center = np.array([ LIMIT/2 for x in range(DIMENSIONS)])

for line in f.readlines():

    line = line.replace(",","")
    line = line.replace("\n","")
    words = line.split(" ")

    random_array = np.array([ random.uniform( 1 , NEW_RATIO ) for x in range(DIMENSIONS) ])

    for word in words:
        new_vector = word_vectors.get( word , center) + random_array
        word_vectors[word.lower()] = new_vector

# Plot the data
plt.ylim(-LIMIT, LIMIT)
plt.xlim(-LIMIT, LIMIT)

for k, v in word_vectors.items():
    plt.text(v[0], v[1], k)
    print("Word:",k)
    print("v 0:",v[0])
    print("v 1:",v[1])
plt.show()

print(word_vectors)
