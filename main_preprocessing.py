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