from Bio import SeqIO
import os

def extract_dloop(genome_record):
    """Function to extract D-loop region from a genome record."""
    dloop_feature = None
    for feature in genome_record.features:
        if feature.type == "D_loop":
            dloop_feature = feature
            break
    
    if dloop_feature:
        dloop_sequence = dloop_feature.extract(genome_record.seq)
        return dloop_sequence
    else:
        return None

def main():
    # Define the path to the workspace
    workspace_path = r"C:\Users\Cliente\Documents\dloop"
    dloop_folder = os.path.join(workspace_path, "dloop")  # Save directly to the desktop

    # Create the dloop folder if it doesn't exist
    if not os.path.exists(dloop_folder):
        os.makedirs(dloop_folder)

    # Change to the directory where the .gbk files are located
    genbank_folder = r"C:\Users\Cliente\Documents\mitofish-novoplasty"

    for root, dirs, files in os.walk(genbank_folder):
        for file_name in files:
            if file_name.endswith(".gbk"):
                print("Processing", file_name)
                try:
                    file_path = os.path.join(root, file_name)
                    genome_record = SeqIO.read(file_path, "genbank")
                    dloop_sequence = extract_dloop(genome_record)
                    
                    if dloop_sequence:
                        output_name = os.path.splitext(file_name)[0] + "_dloop.fasta"
                        output_path = os.path.join(dloop_folder, output_name)
                        with open(output_path, "w") as dloop_output:
                            dloop_output.write(f">{genome_record.id}_D-loop\n{dloop_sequence}\n")
                        print("D-loop extracted and saved for", file_name)
                    else:
                        print("D-loop feature not found in", file_name)
                except Exception as e:
                    print("Error processing", file_name, ":", str(e))

    print("Completed")

if __name__ == "__main__":
    main()
