# Thesis

#my_methods.py, 27_classes_file.py, make_final_dataset.py
#Τα παραπάνω είναι μέθοδοι που έφτιαξα για την προεπεξεργασία των δεδομένων
# my_methods.py: includes the following methods:
  #load_data(path) --> loads data from the .mat files(mat_data) and the data from the .hea files(hea_data) in list forms (e.g. mat_data[0] means first patient)
  #get_label(header) --> returns a list of the labels of a single patient (example of input: header_data[0])
  #get_all_labels(header_data) --> returns a list with all the labels of all the patients (e.g. labels[0] --> [426627000 , 164889003]
  #create_file_27_classes --> creates a test file with the filenames of the data containing 
