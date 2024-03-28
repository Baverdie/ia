import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf

url_cat = r'https://github.com/Baverdie/ia/blob/main/machine_learnibg/dataset/cat/01349c1eb4b8c5b7598648f8e861ad4e.png?raw=true'
resp = requests.get(url_cat, stream=True).raw
image_array_cat = np.asarray(bytearray(resp.read()), dtype="uint8")
print(f'Shape of the image {image_array_cat.shape}')
image_cat = cv2.imdecode(image_array_cat, cv2.IMREAD_COLOR)
plt.axis('off')
plt.imshow(cv2.cvtColor(image_cat, cv2.COLOR_BGR2RGB)) #opencv if BGR color, matplotlib usr RGB so we need to switch otherwise the cat will be blue ... O:)
plt.show()

url_dog = r'https://github.com/Baverdie/ia/blob/main/machine_learnibg/dataset/dog/0579b74157c54c1623ad0a4f4d25bf08.png?raw=true'
resp = requests.get(url_dog, stream=True).raw
image_array_dog = np.asarray(bytearray(resp.read()), dtype="uint8")
print(f'Shape of the image {image_array_dog.shape}')
image_dog = cv2.imdecode(image_array_dog, cv2.IMREAD_COLOR)
plt.axis('off')
plt.imshow(cv2.cvtColor(image_dog, cv2.COLOR_BGR2RGB))
plt.show()