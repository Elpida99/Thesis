import numpy as np
import pandas as pd
from my_methods import load_data
from data_loader import get_sex_age

path1 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_1'
path2 = r'C:\Users\elpid\PycharmProjects\Thesis\Data_500_Hz_2\Dataset_2'

data1, header_data1 = load_data(path1)
print(len(data1), (len(header_data1)))

data2, header_data2 = load_data(path2)
print(len(data2), (len(header_data2)))

all_headers = np.append(np.asarray(header_data1), np.asarray(header_data2), axis=0)

IAVb = '270492004'
RBBB = '59118001'
LBBB = '164909002'
AF = '164889003'
SB = '426177001'
ST = '427084000'

IAVb_list = np.full(shape=1101, fill_value="0")
RBBB_list = np.full(shape=1101, fill_value="0")
LBBB_list = np.full(shape=1101, fill_value="0")
AF_list = np.full(shape=1101, fill_value="0")
SB_list = np.full(shape=1101, fill_value="0")
ST_list = np.full(shape=1101, fill_value="0")


def get_6_classes(all_headers, annotation):
    dlist = np.zeros(1101)
    for i in range(0, all_headers.shape[0]-1):
        tmp = all_headers[i][15].split(':')[1]
        label = tmp.split(',')
        for l in label:
            if l == annotation:
                dlist[i] = "1"

    return dlist

IAVb_list = get_6_classes(all_headers, IAVb)
RBBB_list = get_6_classes(all_headers, RBBB)
LBBB_list = get_6_classes(all_headers, LBBB)
AF_list = get_6_classes(all_headers, AF)
SB_list = get_6_classes(all_headers, SB)
ST_list = get_6_classes(all_headers, ST)


d = {'1dAVb': IAVb_list, 'RBBB': RBBB_list, 'LBBB': LBBB_list, 'SB': SB_list, 'AF': AF_list, 'ST': ST_list}
df = pd.DataFrame(data=d, dtype='int64')
df.to_csv("./data/annotations.csv", index=False)

# ---------------------------------------------------------------------------------------------------------------------

sex_list = []
age_list = []

for header in all_headers:
    age, sex = get_sex_age(header)
    age_list.append(age)
    sex_list.append(sex)

d = {'age': age_list, 'sex': sex_list}
df = pd.DataFrame(data=d)

df.to_csv("./data/attributes.csv", index=False)