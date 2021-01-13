from my_methods import load_data, preprocessing, get_all_labels

path = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz'

data, header_data = load_data(path)

# Get labels - (each list represents the labels of a patient)
labels = get_all_labels(header_data)

"""
Preprocessing (500 Hz freq, 7500 points for each recording(each lead) and T = 15 sec)
    # Zero padding for smaller samples
    # Fixed length 7500 points--> cutting randomly 7500 parts from larger samples
"""
recordings = preprocessing(data)

# normalization???
# bandpass filter???

def bandpass_filter(data, lowcut, highcut, signal_freq, filter_order):
        """
        Method responsible for creating and applying Butterworth filter.
        :param deque data: raw data
        :param float lowcut: filter lowcut frequency value
        :param float highcut: filter highcut frequency value
        :param int signal_freq: signal frequency in samples per second (Hz)
        :param int filter_order: filter order
        :return array: filtered data
        """
        nyquist_freq = 0.5 * signal_freq
        low = lowcut / nyquist_freq
        high = highcut / nyquist_freq
        b, a = butter(filter_order, [low, high], btype="band")
        y = lfilter(b, a, data)
        return y
