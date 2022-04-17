from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
import cv2
import numpy as np
import csv
dict_from_csv = {}

with open('class_dict.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

model = load_model("model.h5")
img=plt.imread("1800.jpg")
img=cv2.resize(img, (112,112))
img=np.expand_dims(img, axis=0)
pred=model.predict(img)
index=np.argmax(pred[0])
klass=dict_from_csv[str(index)]