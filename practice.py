from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Sample aligned corpus of Marathi and Kokani sentences
aligned_corpus = [
    ("मला कुठल्या वेळी तुम्हाला दिल्या जाऊ शकतो?", "कुठल्या वेळी तुझ्या कडे आणखी पाठविलं जाऊ शकतो?"),
    ("तुम्ही कुठल्या वेळी पुणे येऊ शकता?", "कुठल्या वेळी तुम्ही पुणे येऊ शकता?")
    # Add more aligned Marathi-Kokani sentence pairs as needed
]

def translate_marathi_to_kokani(marathi_sentence):
    # Find the closest match in the aligned corpus
    best_match = process.extractOne(marathi_sentence, [pair[0] for pair in aligned_corpus], scorer=fuzz.partial_ratio)
    matched_index = [pair[0] for pair in aligned_corpus].index(best_match[0])
    kokani_translation = aligned_corpus[matched_index][1]
    return kokani_translation

# Example usage
marathi_sentence = "मला कुठल्या वेळी साठी s तुम्हाला दिल्या जाऊ शकतो?"
kokani_translation = translate_marathi_to_kokani(marathi_sentence)
print("Marathi Sentence:", marathi_sentence)
print("Kokani Translation:", kokani_translation)
