import os
from Bio import SeqIO

# Paths to directories
source_folder = r"C:\Users\Cliente\Documents\mitofish-novoplasty"
destination_folder = r"C:\Users\Cliente\Documents\pcgs"

def extract_pcgs(input_file, output_file):
    with open(output_file, 'w') as out_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            # Check if the record is not a tRNA and does not contain "RNA" in the description
            if 'RNA' not in record.description and not record.description.startswith('>tRNA'):
                SeqIO.write(record, out_file, 'fasta')

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate over all files in the source folder and its subdirectories
for subdir, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith('_genes.fa'):
            file_path = os.path.join(subdir, file)

            # Define the output file path
            output_path = os.path.join(destination_folder, file)

            # Execute the extract_pcgs function for each file
            extract_pcgs(file_path, output_path)
            print(f"Function extract_pcgs executed for {file_path}. Output saved in {output_path}")
