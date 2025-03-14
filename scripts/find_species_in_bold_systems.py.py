import xml.etree.ElementTree as ET
import csv

# List of species to search for
species_list = [
    "Heros notatus",
    "Acarichthys heckelii",
    "Pterophyllum scalare",
    "Cichlasoma bimaculatum",
    "Hypselecara temporalis",
    "Satanoperca jurupari",
    "Cichlasoma amazonarum",
    "Cichla monoculus",
    "Chaetobranchopsis orbicularis",
    "Crenicichla notophthalmus",
    "Satanoperca lilith",
    "Crenicichla marmorata",
    "Uaru amphiacanthoides",
    "Symphysodon discus",
    "Acaronia nassa",
    "Geophagus dicrozoster",
    "Cichla temensis",
    "Chaetobranchus flavescens",
    "Crenicichla macrophthalma",
    "Aequidens pallidus",
    "Gymnogeophagus labiatus",
    "Crenicichla lugubris",
    "Biotodoma cupido",
    "Australoheros barbosae",
    "Gymnogeophagus rhabdotus",
    "Apistogramma sp. 'cuieiras'",
    "Astronotus ocellatus",
    "Mesonauta festivus",
    "Arapaima gigas",
    "Colossoma macropomum",
    "Osteoglossum bicirrhosum",
    "Pygocentrus nattereri"
]

# Function to search for species in the XML file
def search_species_in_xml(xml_file):
    # Load and parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all <species> elements and extract the species name
    species_elements = root.findall('.//species/taxon/name')

    # Iterate over the <name> elements and check if they match any species in the list
    found_species = set()
    for species_element in species_elements:
        species_name = species_element.text.strip() if species_element.text else ""
        for species in species_list:
            if species.lower() == species_name.lower():
                found_species.add(species_name)  # Use a set to avoid duplicates
    
    return sorted(found_species)  # Return a sorted list

# Function to save results to a CSV file
def save_to_csv(found_species, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Species Name'])
        for species in found_species:
            writer.writerow([species])

# Path to the XML file and the CSV output file
xml_file = r'C:\Users\Cliente\Downloads\bold_data (1).xml'
csv_file = r'C:\Users\Cliente\Downloads\found_species.csv'

# Execute the function to find species and save the results
found_species = search_species_in_xml(xml_file)
if found_species:
    print("Species found and saved to CSV:")
    for species in found_species:
        print(f"Species name: {species}")
    save_to_csv(found_species, csv_file)
else:
    print("None of the listed species were found in the XML file.")
