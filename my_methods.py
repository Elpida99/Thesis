import numpy as np
import os
import random
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from data_loader import load_challenge_data


# subject/ patient --> data[x]
# sample/ recording/ lead data --> data[x][y]
# signal --> data[x][y][z]


def load_data(path):
	#  hea_data_split = []
	mat_data = []
	hea_data = []
	for file in os.listdir(path):
		f_name, f_ext = os.path.splitext(file)
		if f_ext == '.mat':
			filename = f"{path}\\{f_name}{f_ext}"
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


# def get_filename(header_data):
#     filename = header_data[0].split(' ')[0]
#
#     return filename


def find_27_classes(header_data, labels, dataset="dataset1"):
	header_names = []
	for header in header_data:
		label = get_label(header)
		for lab in label:
			for scored in labels:
				if str(scored) == lab:
					header_filename = header[0].split(' ')[0]
					if dataset == "dataset3":
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


def fix_length(recordings, length):
	processed_recordings = []

	for i in range(0, len(recordings)):
		subj = np.zeros([12, length])
		for j in range(recordings[i].shape[0]):
			lead_samples = np.zeros(length)

			if recordings[i][j].shape[0] < length:
				zeros = length - recordings[i][j].shape[0]
				lead_samples = np.pad(recordings[i][j], (0, zeros), 'constant', constant_values=0)

			elif recordings[i][j].shape[0] > length:
				lead_samples = cut_sample(recordings[i][j], length)

			elif recordings[i].shape[1] == length:
				lead_samples = recordings[i][j]
			subj[j] = lead_samples
		processed_recordings.append(subj)

	return processed_recordings


def cut_sample(sample, length):  # sample is recordings[i][j] (data of a lead)
	tmp = []
	max_range = sample.shape[0] - length
	starting_value = random.randint(0, max_range)
	for i in range(starting_value, starting_value+length):
		tmp.append(sample[i])
	sub_sample = np.asarray(tmp)
	return sub_sample


def normalize_data(processed_recordings):
	normalized_data = []
	for patient in processed_recordings:
		
		scaler = MinMaxScaler(feature_range=(-1, 1))
		scaler.fit(patient)
		norm_subject = scaler.transform(patient)

		normalized_data.append(norm_subject)

	return normalized_data


def print_spectogram(data, title, number):
	plt.figure(number)
	f, t, Sxx = signal.spectrogram(data, fs=500, return_onesided=False)
	plt.pcolormesh(t, fftshift(f), fftshift(Sxx, axes=0), shading='gouraud')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.title(title)
	plt.show()


def bandpass_with_lfilter(data):
	filtered_data = []
	fs = 500
	for subject in data:
		filtered_subject = np.zeros(subject.shape)
		for i in range(0, 11):
			lead = subject[i]
			b = signal.firwin(100, [3, 45], pass_zero='bandpass', fs=fs)
			w, h = signal.freqz(b, worN=7500)  # worN=7500 because test_signal.shape = 7500
			x = lead

			filtered_lead = signal.lfilter(b=b, a=1, x=x)

			filtered_subject[i] = filtered_lead

		filtered_data.append(filtered_subject)
	return filtered_data


def plot_signals(ecg, ecg_after):

	# ------------------------------------------------
	# Plot the original and filtered signals.
	# ------------------------------------------------

	plt.figure()
	fs = 500
	taps = 100
	time = np.arange(ecg.size) / fs

	# the phase delay of the filtered signal:
	delay = 0.5 * (taps - 1) / fs

	plt.plot(time, ecg, time-delay, ecg_after, 'g')
	plt.xlabel("time in s")
	plt.ylabel("ECG in mV")
	plt.title("Patient 0, Lead I")
	plt.legend(('unfiltered signal', 'filtered signal'))
	plt.xlim(0, 3)  # 3 seconds
	plt.ylim(-2, 2)
	plt.show()


def print_all_shapes(data):
	for subject in range(0, len(data)):
		for sample in range(data[subject].shape[0]):
			print(data[subject][sample].shape[0])


def plots(ecg, lead):
	# Sampling Frequency

	fs = 500
	time = np.arange(ecg.size) / fs
	plt.plot(time, ecg)
	plt.xlabel("time in s")
	plt.ylabel("ECG in mV")
	plt.title(f"Lead {lead}")
	plt.xlim(0, 3)
	plt.ylim(-1, 1.5)
	plt.show()
	      
	     
def resample_data(x):
	resampled_x = []

	for sample in x:
		secs = sample.shape[1] / 500
		samples = math.ceil(secs * 400)
		resampled = signal.resample(sample, samples, axis=1)

		resampled_x.append(resampled)

	return resampled_x


def transpose_data(data):
	new_data = []
	for sample in data:
		new_sample = np.transpose(sample)
		new_data.append(new_sample)
	return np.asarray(new_data)
