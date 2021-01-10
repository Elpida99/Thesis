# Thesis

#my_methods.py, 27_classes_file.py, make_final_dataset.py\
#Τα παραπάνω είναι μέθοδοι που έφτιαξα για την προεπεξεργασία των δεδομένων\
# my_methods.py: includes the following methods: 
  #<b>load_data(path)</b> --> loads data from the .mat files(mat_data) and the data from the .hea files(hea_data) in list forms (e.g. mat_data[0] means first patient)\
  #<b>get_label(header)</b> --> returns a list of the labels of a single patient (example of input: header_data[0])\
  #<b>get_all_labels(header_data)</b> --> returns a list with all the labels of all the patients (e.g. labels[0] --> [426627000 , 164889003])\
  #<b>create_file_27_classes(hea_names, dt)</b> --> creates a test file with the filenames of the data of a dataset (dt) containing diagnosis from the 27 scored ones\
  #<b>find_27_classes(header_data, labels, dataset="dataset1)</b> --> finds the filenames and calls create_file_27_classes()\
  #<b>cut_sample(sample)</b>
