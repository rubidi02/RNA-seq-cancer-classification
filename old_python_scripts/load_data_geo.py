import pandas as pd
from pyensembl import EnsemblRelease
import time

#load data from GEO
data_geo = pd.read_csv('../data/data-geo/breast/GSE202203_TPM_Raw_gene_3207.tsv', delimiter='\t', index_col=0)
data_geo = data_geo.transpose()
print(data_geo.columns)

#open the list of genes from tcga

with open(all_data_columns_file_path, 'rb') as all_data_columns_pckl:
    all_data_columns = pickle.load(all_data_columns_pckl)






#replace gene names with Ensembl IDs
# new_col_names = []
# for i in range(len(data_geo.columns)):
#     gene = data_geo.columns[i]
#     try:
#         time.sleep(0.01)
#         ensembl_ID = EnsemblRelease().gene_ids_of_gene_name(gene)[0]
#         new_col_names.append(ensembl_ID)
#     except:
#         print('Error in converting the gene:')
#         print(gene)

# data_geo.columns = new_col_names
# print(data_geo)