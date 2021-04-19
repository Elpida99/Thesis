from my_methods import load_data, get_all_labels, normalize_data, fix_length, plot_signals, bandpass_with_lfilter
from data_loader import get_classes
import numpy as np
import h5py

# ----------------------------------------------------------------------------------------
# Preprocessing (500 Hz freq, 7500 points for each recording(each lead) and T = 15 sec)
# Zero padding for smaller samples
# Fixed length 7500 points--> cutting randomly 7500 parts from larger samples
# ----------------------------------------------------------------------------------------

path1 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_1'
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_2'

def preprocessing(path):
  data, header_data = load_data(path)

  normalized_data = normalize_data(data)

  unfiltered_recordings = fix_length(normalized_data)

  filtered_recordings = bandpass_with_lfilter(unfiltered_recordings)

  return filtered_recordings

dataset1 = preprocessing(path1)
dataset2 = preprocessing(path2)

combined_datasets = np.append(dataset1, dataset2, axis=0)
print(combined_datasets.shape)

with h5py.File(r'C:\Users\elpid\PycharmProjects\Thesis\data\ecg_tracings.hdf5', 'w') as hdf:
     hdf['tracings'] = combined_datasets
hdf.close()
