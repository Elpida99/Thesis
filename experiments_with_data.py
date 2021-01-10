import pandas as pd
import numpy as np
from my_methods import load_data, preprocessing, get_all_labels, find_27_classes

# Paths to the datasets + a test dataset with 20 recordings
path1 = r'C:\Users\elpid\PycharmProjects\Thesis\China 12-Lead ECG Challenge Database'  # Dataset 1
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\CPSC2018 training set'  # Dataset 2
path3 = r'C:\Users\elpid\PycharmProjects\Thesis\Georgia 12-Lead ECG Challenge Database'  # Dataset 3
path4 = r'C:\Users\elpid\PycharmProjects\Thesis\PTB-XL electrocardiography Database'  # Dataset 4
path5 = r'C:\Users\elpid\PycharmProjects\Thesis\PTB Diagnostic ECG Database'  # Dataset 5
path6 = r'C:\Users\elpid\PycharmProjects\Thesis\St Petersburg INCART 12-lead Arrhythmia Database'  # Dataset 6 (Holter samples)
testpath = r'C:\Users\elpid\PycharmProjects\Thesis\Test data'

"""
Frequency:
Dataset 1 : 500 Hz 
Dataset 2 : 500 Hz  
Dataset 3 : 500 Hz  
Dataset 4 : 500 Hz  
Dataset 5 : 1000 Hz 
Dataset 6 : 257 Hz  
"""

# Load 27 classes (SNOMED CT Codes)
df = pd.read_csv('dx_mapping_27_scored.csv')  # 6 pairs of classes always coexist
scored_labels = np.asarray(df['SNOMED CT Code'])

# Load dataset 1 - 3453 recordings

data, header_data = load_data(path3)

# Get labels - 3453 lists (each list represents the labels of a patient)
labels = get_all_labels(header_data)




"""
Preprocessing (500 Hz freq, 7500 points for each recording(each lead) and T = 15 sec)
    # Zero padding for smaller samples
    # Fixed length 7500 points--> cutting randomly 7500 parts from larger samples
"""
# recordings = preprocessing(data)

# Save processed data in hdf5 format

# for header in header_data:
#     print(header[0].split(' ')[2]) prints frequency of every recording


"""
classes = get_classes(testpath)
print("Unique classes:", classes)

print("data[0] --> 1st recording")

info = header_data[0][0]
leadI = header_data[0][1]
leadII = header_data[0][2]
print(info)

print("Lead I:")
print_header_per_lead(leadI)
print("Lead I data:")
print(data[0][0], '\n')

print("Lead II:")
print_header_per_lead(leadII)
print("Lead II data:")
print(data[0][1], '\n')
"""