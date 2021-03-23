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
normalized_data = normalize_2(data)

unfiltered_recordings = fix_length(normalized_data)
