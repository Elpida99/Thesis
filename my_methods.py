import numpy as np
import os
import random

from data_loader import load_challenge_data


def load_data(path):
    # hea_data_split = []
    mat_data = []
    hea_data = []

    for file in os.listdir(path):
        f_name, f_ext = os.path.splitext(file)
        if f_ext == '.mat':
            filename = f"{path}\{f_name}{f_ext}"
            data, header_data = load_challenge_data(filename)
            # dic = parse_header(header_data)
            hea_data.append(header_data)
            # hea_data_split.append(dic)
            mat_data.append(data)
    return mat_data, hea_data  # , hea_data_split


def get_label(header_data):
    for line in header_data:
        if line.startswith('#Dx'):
            label = line.split(': ')[1].split(',')  # [0]

    return label


def get_all_labels(header_data):
    labels = []
    for header in header_data:
        label = get_label(header)
        labels.append(label)
    return labels


def find_27_classes(header_data, labels, dataset="dataset1"):
    header_names = []
    for header in header_data:
        label = get_label(header)
        for lab in label:
            for scored in labels:
                if str(scored) == lab:
                    header_filename = header[0].split(' ')[0]
                    if dataset=="dataset3":
                        header_filename = header_filename.split('.')[0]
                    header_names.append(header_filename)
    create_file_27_classes(header_names, dt=dataset)


def create_file_27_classes(hea_names, dt):
    filename = dt + '.txt'
    with open(filename, 'w') as f:
        for hea_name in hea_names:
            # f.write(f"{hea_name}.hea, ")
            f.write(f"{hea_name}, ")


def print_header_per_lead(lead):
    print(f"filename: {lead.split(' ')[0]}")
    print(f"bits+offset: {lead.split(' ')[1]}")
    print(f"amplitude resolution: {lead.split(' ')[2]}")
    print(f"resolution of ADC converter: {lead.split(' ')[3]}")
    print(f"baseline value: {lead.split(' ')[4]}")
    print(f"first value of signal: {lead.split(' ')[5]}")
    print(f"checksum: {lead.split(' ')[6]}")
    print(f"??: {lead.split(' ')[7]}")
    print(f"name of lead: {lead.split(' ')[8]}")

          
def fix_length(recordings):
	processed_recordings = []

	for i in range(0, len(recordings)):
		subj = np.zeros([12, 7500])
		for j in range(recordings[i].shape[0]):
			lead_samples = np.zeros(7500)

			if recordings[i][j].shape[0] < 7500:
				zeros = 7500 - recordings[i][j].shape[0]
				lead_samples = np.pad(recordings[i][j], (0, zeros), 'constant', constant_values=0)

			elif recordings[i][j].shape[0] > 7500:
				lead_samples = cut_sample(recordings[i][j])

			elif recordings[i].shape[1] == 7500:
				lead_samples = recordings[i][j]
			subj[j] = lead_samples
		processed_recordings.append(subj)

	return processed_recordings


def cut_sample(sample):  # sample is recordings[i][j] (data of a lead)
	tmp = []
	max_range = sample.shape[0] - 7500
	starting_value = random.randint(0, max_range)
	for i in range(starting_value, starting_value+7500):
		tmp.append(sample[i])
	sub_sample = np.asarray(tmp)
	return sub_sample
          
def normalize(processed_recordings):
	normalized_data = []
	for patient in processed_recordings:
		scaler = MinMaxScaler(feature_range=(-1, 1))
		scaler.fit(patient)
		norm_subject = scaler.transform(patient)

		normalized_data.append(norm_subject)

	return normalized_data


def print_all_shapes(data):
    for subject in range(0, len(data)):
        for sample in range(data[subject].shape[0]):
            print(data[subject][sample].shape[0])
