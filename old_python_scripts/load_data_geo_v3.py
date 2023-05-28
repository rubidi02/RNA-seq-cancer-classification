import pandas as pd
import mygene

# Load gene expression data from TSV file
data_path = '../data/data-geo/breast/GSE202203_TPM_Raw_gene_3207.tsv'
df = pd.read_csv(data_path, sep='\t', index_col=0)

# Create a mygene client to map gene symbols and synonyms to Ensembl IDs
mg = mygene.MyGeneInfo()

# Map gene symbols and synonyms to Ensembl IDs
ensembl_ids = mg.querymany(df.index.tolist(), scopes=['symbol', 'alias'], fields='ensembl.gene', species='human', returnall=True)

# Create a dictionary of gene symbol to Ensembl ID mappings
symbol_to_ensembl = {}
for x in ensembl_ids['out']:
    if 'ensembl' in x:
        if isinstance(x['ensembl'], list):
            # Use the first element of the list as the Ensembl ID
            symbol_to_ensembl[x['query']] = x['ensembl'][0]['gene']
        else:
            # Use the Ensembl ID directly if it is not a list
            symbol_to_ensembl[x['query']] = x['ensembl']['gene']
    else:
        # Handle no hits by setting the Ensembl ID to None
        symbol_to_ensembl[x['query']] = None

# Print the number of duplicate and missing hits
print(f"{len(ensembl_ids['dup'])} input query terms found dup hits.")
print()
print(f"{len(ensembl_ids['missing'])} input query terms found no hit.")

# Add a new column to the data frame with Ensembl IDs
df['ensembl_id'] = df.index.map(symbol_to_ensembl)

# Save the results to a new file
output_path = '../data/data-geo/breast/GSE202203_TPM_Raw_gene_3207_with_ensembl.tsv'
df.to_csv(output_path, sep='\t')
