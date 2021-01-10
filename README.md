# Thesis

#my_methods.py, 27_classes_file.py, make_final_dataset.py\
#Τα παραπάνω είναι μέθοδοι που έφτιαξα για την προεπεξεργασία των δεδομένων
# my_methods.py: includes the following methods: 
  * <b>load_data(path)</b> --> loads data from the .mat files(mat_data) and the data from the .hea files(hea_data) in list forms (e.g. mat_data[0] means first patient)
  * <b>get_label(header)</b> --> returns a list of the labels of a single patient (example of input: header_data[0])
  * <b>get_all_labels(header_data)</b> --> returns a list with all the labels of all the patients (e.g. labels[0] --> [426627000 , 164889003])
  * <b>create_file_27_classes(hea_names, dt)</b> --> creates a text file (e.g. 'dataset.txt') with the filenames of the data of a dataset (dt) containing diagnosis from the 27 scored ones
  * <b>find_27_classes(header_data, labels, dataset="dataset1")</b> --> finds the filenames and calls create_file_27_classes()
  * <b>cut_sample(sample)</b> --> returns randoms fixed width windows (7500 points) from larger samples
  * <b>preprocessing(recordings)</b> --> (recordings = mat_data) implements zero padding to smaller samples and calls <b>cut_samples</b> for larger ones

# 27_classes_file.py: includes the following methods:
  * <b>save_27_classes_files(path, scored_labels, datast)</b> --> calls <b>find_27_classes</b> and creates and saves the text files
  * calls the above method for every dataset

# make_final_dataset.py: includes the following methods:
* <b>final_dataset(filename)</b> --> reads the text files (e.g 'dataset.txt') and returns an array with the unique filenames(some patients have more than one diagnosis from the 27).
* <b>cp_data_to_final_directory(path, new_p, fnl_dataset)</b> --> takes as input the final_dataset returned from the above method and copys all files that contain labels of the 27 scored ones in the directory "Data_500_Hz"
# Final result:
* Directory 'Data_500_Hz' contains <b>18271</b> recordings from 4 datasets.
* Each recording belongs to one or more of the 27 scored classes. 
* After preprocessing all recordings have length equal to 7500 points.
