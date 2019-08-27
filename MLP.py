# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:52:14 2019

@author: Artemis
"""
"""
import numpy as np
import matplotlib.pyplot as plt

line = np.linspace(-5, 5, 200)

plt.plot(line, np.tanh(line), label='tanh')
plt.plot(line, np.maximum(line, 0), label='relu')

plt.legend(loc='best')

plt.xlabel('x')
plt.ylabel('relu(x) and tanh(x)')

plt.show()
"""

"""
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

wine = load_wine()
X = wine.data[:,:2]
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[10,10],
                    activation='tanh', alpha=1)
mlp.fit(X_train, y_train)

cmap_light = ListedColormap(['#FFAAAA','#AAFFAA','#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000','#00FF00','#0000FF'])
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

plt.title("MLPClassifier: solver=lbfgs")

plt.show()
"""

from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from PIL import Image
import numpy as np

mnist = fetch_mldata('mnist-original')

X = mnist.data/255.
y = mnist.target

X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=5000, test_size=1000, random_state=62)

mlp_hw = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[100,100],
                       activation='relu', alpha=1e-5, random_state=62)

mlp_hw.fit(X_train, y_train)
print("Score:{:.2f}%".format(mlp_hw.score(X_test, y_test)*100))

image = Image.open('data/4.jpg').convert('F')
image = image.resize((28,28))
arr = []
for i in range(28):
    for j in range(28):
        pixel = 1.0 - float(image.getpixel((j,i))) / 255.
        arr.append(pixel)
arr_1 = np.array(arr).reshape(1, -1)
print('The number in the image: {:.0f}'.format(mlp_hw.predict(arr_1)[0]))
pass