import pandas as pd
import numpy as np
from my_methods import load_data, get_all_labels, find_27_classes

# Paths to the datasets
path1 = r'C:\Users\elpid\PycharmProjects\Thesis\China 12-Lead ECG Challenge Database'  # Dataset 1 500 Hz
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\CPSC2018 training set'  # Dataset 2 500 Hz
path3 = r'C:\Users\elpid\PycharmProjects\Thesis\Georgia 12-Lead ECG Challenge Database'  # Dataset 3 500 Hz
path4 = r'C:\Users\elpid\PycharmProjects\Thesis\PTB-XL electrocardiography Database'  # Dataset 4 500 Hz


def save_27_classes_files(path, scored_labels, datast):
    # Load dataset
    data, header_data = load_data(path)

    find_27_classes(header_data, scored_labels, dataset=datast)


# Load 27 classes (SNOMED CT Codes)
df = pd.read_csv('dx_mapping_27_scored.csv')  # 6 pairs of classes always coexist??
scored_labels = np.asarray(df['SNOMED CT Code'])

paths = [path1, path2, path3, path4]
for i in range(1, 5):
    data_name = f"dataset{i}"
    save_27_classes_files(paths[i-1], scored_labels, datast=data_name)
