import pathlib
import os
import tensorflow as tf

data_dir = tf.keras.utils.get_file(
	"dataset.zip",
	"/datasets/dataset.zip",
	extract=False)

import zipfile
with zipfile.ZipFile(data_dir, 'r') as zip_ref:
	zip_ref.extractall('/content/datasets')

data_dir = pathlib.Path('/content/datasets/dataset')
print(data_dir)
print(os.path.abspath(data_dir))