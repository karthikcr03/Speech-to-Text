import spacy
import json

# Load spaCy's Transformer model (for better accuracy) - you can use "en_core_web_sm" for speed
nlp = spacy.load("en_core_web_trf")  

# Read text from the input file
with open("transcription.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with spaCy
doc = nlp(text)

# Initialize variables to store extracted details
enquirer_name = ""
enquirer_place = ""
beneficiary_name = ""
beneficiary_age = ""
destination_place = ""

# Loop through named entities to extract information
for ent in doc.ents:
    if ent.label_ == "PERSON" and not enquirer_name:  
        enquirer_name = ent.text  # First person is the enquirer
    elif ent.label_ == "GPE":
        if not enquirer_place:
            enquirer_place = ent.text  # First location is enquirer's place
        else:
            destination_place = ent.text  # Second location is destination
    elif ent.label_ == "PERSON":
        beneficiary_name = ent.text  # Next person detected is beneficiary
    elif ent.label_ == "CARDINAL" or ent.label_ == "AGE":
        beneficiary_age = ent.text  # Extract age if mentioned

# Create the output JSON
output_data = {
    "Enquired person name": enquirer_name,
    "Place": enquirer_place,
    "Beneficiary name": beneficiary_name,
    "Age": beneficiary_age,
    "Place to look": destination_place
}

# Save extracted data as a JSON file
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, indent=4)

print("✅ Extraction complete! Output saved in 'output.json'.")
