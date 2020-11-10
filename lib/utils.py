import os
import urllib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import validators
from pathlib import Path

KAGGLE_DIR_GIT = "https://github.com/brtonnies/face-mask-detection/blob/main/data/images"
CMFD_DIR_GIT = "https://github.com/brtonnies/face-mask-detection/blob/main/data/images/CMFD/images"
IMFD_DIR_GIT = "https://github.com/brtonnies/face-mask-detection/blob/main/data/images/IMFD/images"

ROOT_DIR = Path(os.getcwd()).parent()
DATA_DIR = os.path.join(ROOT_DIR, 'data')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')
ANNOTATIONS_DIR = os.path.join(DATA_DIR, 'annotations')
SUB_IMAGES_DIR = os.path.join(IMAGES_DIR, 'sub')


def get_image(name, source='kaggle', options=None):
    if source.lower() in ['kaggle', 'kagg', 'kag']:
        source_url = KAGGLE_DIR_GIT
    elif source.lower() in 'cmfd':
        source_url = CMFD_DIR_GIT
    elif source.lower() == 'imfd':
        source_url = IMFD_DIR_GIT
    else:
        source_url = None

    url = os.path.join(source_url, "{}?raw=true".format(name))
    resp = urllib.request.urlopen(url)

    if options is not None and len(options.keys()) > 0:
        if 'lib' in options.keys() and options['lib'] == 'cv2':
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        elif 'format' in options.keys() and options['format'] is not None:
            image = plt.imread(resp, format=options['format'])
        else:
            image = plt.imread(resp)
    else:
        image = plt.imread(resp)

    return image


def get_kaggle_img(name, options=None):
    options['format'] = name.split(".")[-1]
    url = os.path.join(KAGGLE_DIR_GIT, "{}?raw=true".format(name))
    image = get_image(url, options)
    return image


def get_cmfd_img(name, options=None):
    options['format'] = name.split(".")[-1]
    url = os.path.join(CMFD_DIR_GIT, "{}?raw=true".format(name))
    return get_image(url, options)


def get_imfd_img(name, options=None):
    options['format'] = name.split(".")[-1]
    url = os.path.join(IMFD_DIR_GIT, "{}?raw=true".format(name))
    return get_image(url, options)
