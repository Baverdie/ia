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

url_cat = r'https://github.com/Baverdie/ia/blob/main/machine_learnibg/cat.png?raw=true'
resp = requests.get(url_cat, stream=True).raw
image_array_cat = np.asarray(bytearray(resp.read()), dtype="uint8")
print(f'Shape of the image {image_array_cat.shape}')
image_cat = cv2.imdecode(image_array_cat, cv2.IMREAD_COLOR)
plt.axis('off')
plt.imshow(cv2.cvtColor(image_cat, cv2.COLOR_BGR2RGB))
plt.show()

url_dog = r'https://github.com/Baverdie/ia/blob/main/machine_learnibg/dog.png?raw=true'
resp = requests.get(url_dog, stream=True).raw
image_array_dog = np.asarray(bytearray(resp.read()), dtype="uint8")
print(f'Shape of the image {image_array_dog.shape}')
image_dog = cv2.imdecode(image_array_dog, cv2.IMREAD_COLOR)
plt.axis('off')
plt.imshow(cv2.cvtColor(image_dog, cv2.COLOR_BGR2RGB))
plt.show()


import pathlib
import os
data_dir = tf.keras.utils.get_file(
    "dataset.zip",
    "https://github.com/Baverdie/ia/blob/main/machine_learnibg/dataset.zip?raw=true",
    extract=False)

import zipfile
with zipfile.ZipFile(data_dir, 'r') as zip_ref:
    zip_ref.extractall('/content/datasets')

data_dir = pathlib.Path('/content/datasets/dataset')
print(data_dir)
print(os.path.abspath(data_dir))

image_count = len(list(data_dir.glob('*/*')))
print(image_count)