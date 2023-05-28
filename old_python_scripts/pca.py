import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the data from pickle files
all_data = pd.read_pickle("all_data.pkl")
all_labels = pd.read_pickle("all_labels.pkl")

scaler = StandardScaler()
all_data = scaler.fit_transform(all_data)

# Perform PCA on the data
pca = PCA(n_components=3)
transformed_data = pca.fit_transform(all_data)

# Convert string labels to numerical labels
label_encoder = LabelEncoder()
all_labels_encoded = label_encoder.fit_transform(all_labels)

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(transformed_data[:, 0], transformed_data[:, 1], transformed_data[:, 2], c=all_labels_encoded)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
plt.show()


