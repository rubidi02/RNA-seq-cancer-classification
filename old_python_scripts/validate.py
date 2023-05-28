import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from gtfparse import read_gtf

# #load model
# model_file_name = 'cancer_xgboost.model'

# with open(model_file_name, 'rb') as model_file:
#     model = pickle.load(model_file)

# #load validation data
# val_data = 'all_data.pkl'
# val_labels = 'all_labels.pkl'

# with open(val_data, 'rb') as data_file:
#     all_data = pickle.load(data_file)

# with open(val_labels, 'rb') as labels_file:
#     all_labels = pickle.load(labels_file)

# #encode labels
# label_encoder = LabelEncoder()
# all_labels_encoded = label_encoder.fit_transform(all_labels[0].to_list())

# #predictions
# val_pred = model.predict(all_data)

# accuracy = accuracy_score(val_pred, all_labels_encoded)
# print("Accuracy of the test: %.4f%%" % (accuracy * 100.0))


#load gtf file
df = read_gtf("../data/data-geo/breast/GSE202203_UCSC_hg38_knownGenes_22sep2014.gtf")
print(df[:10]["knownToRefSeq"])