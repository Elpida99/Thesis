import numpy as np
import h5py
from my_methods import (bandpass_filter, fix_length, load_data, make_float_32,
                        normalize_data, resample_data, transpose_data, mV)

# ----------------------------------------------------------------------------------------
# Preprocessing (500 Hz freq, 7500 points for each recording(each lead) and T = 15 sec)
# Zero padding for smaller samples
# Fixed length 7500 points--> cutting randomly 7500 parts from larger samples
# ----------------------------------------------------------------------------------------

path1 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_1'
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_2'


def main_preprocessing(path, length):
  """
  Normalizes the data to [-1, 1] and if pretrained is True, they are resampled
  Applies zero padding/ cuts the recordings to a fixed length
  Applies banpass filter
  :param path: path to dataset
  :param length: desired length of recordings
  :param pretrained: if the data are meant for the pretrained model then set to True
  :return: the final processed data
  """
  data, header_data = load_data(path)

  normalized_data = normalize_data(data)

  unfiltered_recordings = fix_length(normalized_data, length)

  filtered_recordings = bandpass_filter(unfiltered_recordings, 500)

  return filtered_recordings


def main_data(path1, path2):
  dataset1 = main_preprocessing(path1, 7500)
  dataset2 = main_preprocessing(path2, 7500)

  combined_datasets = np.append(dataset1, dataset2, axis=0)
  print(combined_datasets.shape)

  with h5py.File(r'C:\Users\elpid\PycharmProjects\Thesis\data\ecg_tracings.hdf5', 'w') as hdf:
       hdf['tracings'] = combined_datasets
  hdf.close()


def pretrained_preprocessing(path, length):
  data, header_data = load_data(path)

  resampled_data = resample_data(data, 500, 400)

  normalized_data = normalize_data(resampled_data)

  unfiltered_recordings = fix_length(normalized_data, length)

  # filtered_recordings = bandpass_filter(unfiltered_recordings, 400)

  transposed_data = transpose_data(unfiltered_recordings)

  final_data = make_float_32(transposed_data)

  final_dataset = mV(final_data)

  return final_dataset


def pretrained_data(path1, path2):
  """
  :param path1: path to dataset 1
  :param path2: path to dataset 2
  :saves the data in order to be fed in the pretrained model
  """
  dataset1 = pretrained_preprocessing(path1, 4096)
  dataset2 = pretrained_preprocessing(path2, 4096)

  combined_datasets = np.append(dataset1, dataset2, axis=0)
  print(combined_datasets.shape)

  with h5py.File(r'C:\Users\elpid\PycharmProjects\Thesis_pretrained\02data_400\test_tracings.hdf5', 'w') as hdf:
    hdf['tracings'] = combined_datasets
  hdf.close()

# main_data(path1, path2)
pretrained_data(path1, path2)

