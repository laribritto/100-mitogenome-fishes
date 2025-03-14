import os
import pandas as pd

# Base directory where folders with VCF files are located
base_dir = '~/Heteroplasmia/numts'  # Replace with your actual base directory
output_dir = '~/estatisticas-heteroplasmia'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to process VCF files within a folder
def process_vcf_files(folder_path, scientific_name):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.vcf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    if not line.startswith('#'):
                        columns = line.strip().split('\t')
                        chrom, pos, id_, ref, alt, qual, filter_, info = columns
                        info_dict = {item.split('=')[0]: item.split('=')[1] if '=' in item else item for item in info.split(';')}
                        af = info_dict.get('AF', None)
                        dp = info_dict.get('DP', None)
                        fr = info_dict.get('FR', None)
                        lcr = info_dict.get('LCR', None)
                        data.append([scientific_name, ref, alt, af, dp, fr, lcr])
    return data

# Iterate over folders in the base directory
all_data = []
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.isdir(folder_path):
        # Extract SRA and scientific name from the folder name
        parts = folder_name.split('_')
        if len(parts) >= 2:
            scientific_name = '_'.join(parts[1:])
            # Process VCF files within the folder
            folder_data = process_vcf_files(folder_path, scientific_name)
            all_data.extend(folder_data)

# Create a dataframe from the collected data
df = pd.DataFrame(all_data, columns=['Scientific name', 'REF', 'ALT', 'AF', 'DP', 'FR', 'LCR'])

# Group by scientific name and save as separate CSV files
for scientific_name, group in df.groupby('Scientific name'):
    output_path = os.path.join(output_dir, f'{scientific_name.replace(" ", "_")}.csv')
    group.to_csv(output_path, index=False)
    print(f'Saved: {output_path}')
