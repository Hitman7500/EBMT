marathi_file_path = "marathi_dataset_corrected.txt"
konakni_file_path = "konkani_dataset_cleaned.txt"
output_file_path = "parallel_sentences.txt"

try:
    with open(marathi_file_path, 'r', encoding='utf-8') as marathi_file, \
            open(konakni_file_path, 'r', encoding='utf-8') as konkani_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:

        for marathi_line, konkani_line in zip(marathi_file, konkani_file):
            # Split by tab ('\t') instead of a space
            output_line = f"{marathi_line.strip()}\t{konkani_line.strip()}\n"
            output_file.write(output_line)

    print("Files joined successfully.")

except FileNotFoundError:
    print("One of the input files not found.")
except Exception as e:
    print("An error occurred:", e)
