import numpy as np
import os
import shutil

from my_methods import load_data

path1 = r'C:\Users\elpid\PycharmProjects\Thesis\China 12-Lead ECG Challenge Database'
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\CPSC2018 training set'  # Dataset 2
path3 = r'C:\Users\elpid\PycharmProjects\Thesis\Georgia 12-Lead ECG Challenge Database'  # Dataset 3
path4 = r'C:\Users\elpid\PycharmProjects\Thesis\PTB-XL electrocardiography Database'  # Dataset 4
new_path = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz'


def final_dataset(filename):
    final_data = []
    f = open(filename)
    for line in f.readlines():
        tmp = line.split(", ")
        for p in tmp:
            final_data.append(p)
    return np.unique(np.asarray(final_data))


def cp_data_to_final_directory(path, new_p, fnl_dataset):
    for file in os.listdir(path):
        f_name, f_ext = os.path.splitext(file)
        for i in range(0, fnl_dataset.shape[0]):
            if f_name == fnl_dataset[i]:
                full_path = f"{path}\{f_name}{f_ext}"
                shutil.copy(full_path, new_p)


# final_d1 = final_dataset("dataset1.txt")
# print(final_d1.shape)
# cp_data_to_final_directory(path1, new_path, final_d1)

# final_d2 = final_dataset("dataset2.txt")
# cp_data_to_final_directory(path2, new_path, final_d2)
# print(final_d2.shape)

# final_d3 = final_dataset("dataset3.txt")
# cp_data_to_final_directory(path3, new_path, final_d3)
# print(final_d3.shape)

final_d4 = final_dataset("dataset4.txt")
cp_data_to_final_directory(path4, new_path, final_d4)
print(final_d4.shape)

data, header_data = load_data(new_path)
print(len(data))
print(len(header_data))
