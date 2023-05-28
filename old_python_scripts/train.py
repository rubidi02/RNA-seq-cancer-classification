import pickle
import xgboost as xgb
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


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

#Split dataset into training and testing sets
all_data_train, all_data_test, all_labels_encoded_train, all_labels_encoded_test = train_test_split(all_data, all_labels_encoded, test_size=0.2, random_state=42)


duplicated = all_data_train.columns[all_data_train.columns.duplicated()]
print(duplicated)

print("Training the model...")

model_train : xgb.XGBClassifier = xgb.XGBClassifier()
model_train.fit(all_data_train, all_labels_encoded_train)

print("Done. Verifying accuracy...")

# verify accuracy of the train data
pred_train = model_train.predict(all_data_train)

accuracy = accuracy_score(pred_train, all_labels_encoded_train)
print("Accuracy of the train: %.4f%%" % (accuracy * 100.0))

# verify accuracy of the test data
pred_test = model_train.predict(all_data_test)

accuracy = accuracy_score(pred_test, all_labels_encoded_test)
print("Accuracy of the test: %.4f%%" % (accuracy * 100.0))

#saving the model for later use
model_file_name = 'cancer_xgboost.model'

with open(model_file_name, 'wb') as file_model:
    pickle.dump(model_train, file_model)