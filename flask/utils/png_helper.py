import cv2
import torch
import numpy as np
from utils.cartex.decomposition import CartoonTextureDecomposition
from utils.irma.irma_reader import get_irma_code

def preprocessing(img):
    decomposer = CartoonTextureDecomposition()
    cartoon, texture = decomposer.decompose(img)
    img = np.expand_dims(img, axis=0)
    cartoon = np.expand_dims(cartoon, axis=0)
    texture = np.expand_dims(texture, axis=0)
    data = np.concatenate((img, cartoon, texture), axis=0).astype('float32')
    return data

def annotate_png(img, model, p):
    """ Predict the probability of a class """
    img = np.array(img)
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
    data = preprocessing(img).astype('float32')
    outputs = model(torch.Tensor(np.expand_dims(data, axis=0)))
    preds = torch.max(outputs, 1)[1]
    return get_irma_code(p.class_names[preds.tolist()[0]])
