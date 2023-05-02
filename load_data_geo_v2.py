import pandas as pd
import requests
import pickle

# Load TSV file with gene names as rows and sample IDs as columns
gene_expression = pd.read_csv('../data/data-geo/breast/GSE202203_TPM_Raw_gene_3207.tsv', sep='\t', index_col=0)

# Transpose the dataframe
gene_expression_transposed = gene_expression.T

# Define a function to convert gene name to Ensembl ID
def get_ensembl_id(gene_name):
    # Make a request to the Ensembl REST API to get the Ensembl ID
    url = f'https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}?expand=1'
    response = requests.get(url, headers={'Content-Type': 'application/json'})
    if response.ok:
        data = response.json()
        if 'id' in data:
            return data['id']
    # If Ensembl ID not found, check for gene aliases and synonyms
    url = f'https://rest.ensembl.org/xrefs/symbol/homo_sapiens/{gene_name}?object_type=gene'
    response = requests.get(url, headers={'Content-Type': 'application/json'})
    if response.ok:
        data = response.json()
        for item in data:
            if item['dbname'] == 'HGNC':
                alias_name = item['display_id']
                # Recursively call get_ensembl_id() with the alias name
                return get_ensembl_id(alias_name)
            elif item['dbname'] == 'SYMBOL':
                synonym_name = item['display_id']
                # Recursively call get_ensembl_id() with the synonym name
                return get_ensembl_id(synonym_name)
    # If gene not found, return None
    print('Didn\'t find gene:')
    print(gene_name)
    return None

# Convert column names to Ensembl IDs
gene_expression_transposed.columns = [get_ensembl_id(gene_name) for gene_name in gene_expression_transposed.columns]

# Pickle the transposed dataframe with Ensembl IDs
with open('gene_expression_transposed.pkl', 'wb') as f:
    pickle.dump(gene_expression_transposed, f)