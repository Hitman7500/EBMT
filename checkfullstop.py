def add_full_stop(sentence):
    # Check if the sentence ends with a full stop
    if sentence.endswith('.'):
        return sentence
    else:
        # Add a full stop at the end
        return sentence.strip() + '.'

# Read Marathi dataset from file
file_path = "marathi_dataset.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    marathi_dataset = file.readlines()

# Check and add full stops where necessary
corrected_marathi_dataset = [add_full_stop(sentence.strip()) for sentence in marathi_dataset]

# Write corrected dataset to a new file
output_file_path = "marathi_dataset_corrected.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    for sentence in corrected_marathi_dataset:
        file.write(sentence + "\n")

print("Full stops added where necessary. Corrected dataset saved to:", output_file_path)
