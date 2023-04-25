import pickle
import xgboost as xgb
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder


# Load ALL data
# all_data_file_path = "all_data.pkl"
# all_labels_file_path = "all_labels.pkl"

# Load REDUCED data
all_data_file_path = "reduced_data.pkl"
all_labels_file_path = "reduced_labels.pkl"

with open(all_data_file_path, 'rb') as all_data_pckl:
    all_data: pd.DataFrame = pickle.load(all_data_pckl)
with open(all_labels_file_path, 'rb') as all_labels_pckl:
    all_labels = pickle.load(all_labels_pckl)

print(all_data)
print(all_labels)

label_encoder = LabelEncoder()
all_labels_encoded = label_encoder.fit_transform(all_labels[0].to_list())
print(all_labels_encoded)

xgb_cl = xgb.XGBClassifier()
xgb_cl.fit(all_data.transpose(), all_labels_encoded)

