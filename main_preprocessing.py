from my_methods import load_data, get_all_labels, normalize_data, fix_length, plot_signals, bandpass_with_lfilter
from data_loader import get_classes
import numpy as np

path = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_1'

data, header_data = load_data(path)

# Get labels - (each list represents the labels of a patient)

labels = get_all_labels(header_data)
# print(labels)
classes = get_classes(path)
# print("Unique classes:", classes)

# ----------------------------------------------------------------------------------------
# Preprocessing (500 Hz freq, 7500 points for each recording(each lead) and T = 15 sec)
# Zero padding for smaller samples
# Fixed length 7500 points--> cutting randomly 7500 parts from larger samples
# ----------------------------------------------------------------------------------------

normalized_data = normalize_data(data)

unfiltered_recordings = fix_length(normalized_data)

filtered_recordings = bandpass_with_lfilter(unfiltered_recordings)

np.save('filtered_1.npy', filtered_recordings)
