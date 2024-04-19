import re

def remove_special_characters(sentence):
    # Define regular expression to match Marathi characters
    marathi_chars = '[\u0900-\u097F]+'

    # Remove numbers, punctuation, bullet points, |, (), and !
    sentence = re.sub(r'[०-९:.,\-\(\)\?•|!“”]', '', sentence)
    # Remove other punctuation except full stops
    sentence = re.sub(r'[^\w\s।' + marathi_chars + ']', '', sentence)
    return sentence.strip()  # Strip leading and trailing spaces

# Read Marathi dataset from file
file_path = "konkani.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    marathi_dataset = file.readlines()

# Remove special characters from Marathi dataset
cleaned_marathi_dataset = [remove_special_characters(sentence.strip()) for sentence in marathi_dataset]

# Write cleaned dataset to a new file
output_file_path = "konkani_dataset_cleaned.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    for sentence in cleaned_marathi_dataset:
        file.write(sentence + "\n")

print("Special character removal completed. Cleaned dataset saved to:", output_file_path)
