import pickle

# Load ALL data
# all_data_file_path = "all_data.pkl"
# all_labels_file_path = "all_labels.pkl"

# Load REDUCED data
all_data_file_path = "reduced_data.pkl"
all_labels_file_path = "reduced_labels.pkl"

with open(all_data_file_path, 'rb') as all_data_pckl:
    all_data = pickle.load(all_data_pckl)
with open(all_labels_file_path, 'rb') as all_labels_pckl:
    all_labels = pickle.load(all_labels_pckl)

print(all_data)
print(all_labels)