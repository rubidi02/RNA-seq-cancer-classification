import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the data from pickle files
all_data = pd.read_pickle("all_data.pkl")
all_labels = pd.read_pickle("all_labels.pkl")

# Normalize the data
scaler = StandardScaler()
all_data = scaler.fit_transform(all_data)

# Perform t-SNE on the data
tsne = TSNE(n_components=3)
transformed_data = tsne.fit_transform(all_data)

# Convert string labels to numerical labels
label_encoder = LabelEncoder()
all_labels_encoded = label_encoder.fit_transform(all_labels)

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(transformed_data[:, 0], transformed_data[:, 1], transformed_data[:, 2], c=all_labels_encoded)
ax.set_xlabel('TSNE 1')
ax.set_ylabel('TSNE 2')
ax.set_zlabel('TSNE 3')
plt.show()
