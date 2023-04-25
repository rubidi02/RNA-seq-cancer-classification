
import pickle

# load data from pickled complete dataset
all_data_file_path = "all_data.pkl"
all_labels_file_path = "all_labels.pkl"
with open(all_data_file_path, 'rb') as all_data_pckl:
    all_data = pickle.load(all_data_pckl)
with open(all_labels_file_path, 'rb') as all_labels_pckl:
    all_labels = pickle.load(all_labels_pckl)

# reduce the data so we can work with it more flexibly
reduced_data = all_data[:100]
reduced_labels = all_labels[:100]

# save new reduced data to pickle for easier loading when trainin
reduced_data_file_path = "reduced_data.pkl"
reduced_labels_file_path = "reduced_labels.pkl"
with open(reduced_data_file_path, 'wb') as reduced_data_pckl:
    pickle.dump(reduced_data, reduced_data_pckl)
with open(reduced_labels_file_path, 'wb') as reduced_labels_pckl:
    pickle.dump(reduced_labels, reduced_labels_pckl)

