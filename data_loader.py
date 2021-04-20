"""
data_loader.py
--------------
This module provides classes and methods for formatting the Physionet2020 dataset.
By: Sebastian D. Goodfellow, Ph.D., 2020

github.com/Seb-Good/physionet-challenge-2020/blob/c6f1648a148335babc0a26d8a589120616327548/kardioml/data/data_loader.py#L14
"""

import os
import numpy as np
from scipy.io import loadmat

from get_12_ECG_features import get_12ECG_features


def load_challenge_data(filename):
    x = loadmat(filename)
    data = np.asarray(x['val'], dtype=np.float64)

    new_file = filename.replace('.mat', '.hea')
    input_header_file = os.path.join(new_file)

    with open(input_header_file, 'r') as f:
        header_data = f.readlines()

    return data, header_data


# Find unique classes.
def get_classes(input_directory):
    """
    based on "get_classes" in https://github.com/physionetchallenges/python-classifier-2020/blob/master/train_12ECG_classifier.py

    """
    classes = set()
    for file in os.listdir(input_directory):
        f_name, f_ext = os.path.splitext(file)
        if f_ext == '.hea':
            file_to_open = input_directory+"\\"+file
            with open(file_to_open, 'r') as f:
                for l in f:
                    if l.startswith('#Dx'):
                        tmp = l.split(': ')[1].split(',')
                        for c in tmp:
                            classes.add(c.strip())
    return sorted(classes)


def get_sex(sex):
    """Return a consistent sex notation (male, female)."""
    if sex.lower() == 'm':
        return 'male'
    if sex.lower() == 'f':
        return 'female'
    return sex.lower()


def get_sex_age(header_data):
    # Elpida Makri
    age = header_data[13].split(':')[-1].strip()
    sex = get_sex(sex=header_data[14].split(':')[-1].strip())

    return age, sex


def parse_header(header_data, inference=False):
    filename = header_data[0].split(' ')[0]
    num_leads = int(header_data[0].split(' ')[1])
    fs = int(header_data[0].split(' ')[2])
    length = int(header_data[0].split(' ')[3])
    date = header_data[0].split(' ')[4]
    time = header_data[0].split(' ')[5]
    amp_conversion = int(header_data[1].split(' ')[2].split('/')[0])
    channel_order = [row.split(' ')[-1].strip() for row in header_data[1:13]]
    age = header_data[13].split(':')[-1].strip()
    sex = get_sex(sex=header_data[14].split(':')[-1].strip())
    if inference:
        labels_snomedct = None
    else:
        labels_snomedct = [int(label) for label in header_data[15].split(':')[-1].strip().split(',')]

    return {'filename': filename, 'date': date, 'time': time, 'channel_order': channel_order, 'age': age, 'sex': sex,
            'labels_SNOMEDCT': labels_snomedct, 'amp_conversion': amp_conversion, 'fs': fs,
            'length': length, 'num_leads': num_leads}


