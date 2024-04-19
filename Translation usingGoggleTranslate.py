from translate import Translator

print("\nINDIAN LANGUAGE TRANSLATOR\n")
print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(India) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")

say_lang = input("\nENTER THE LANGUAGE IN WHICH YOU ARE FAMILIAR WITH (ENTER THE LANG_CODE): ")
convert_lang = input("\nENTER THE LANGUAGE YOU WANT TO CONVERT INTO (ENTER THE LANG_CODE): ")

translator = Translator(from_lang=say_lang, to_lang=convert_lang)

# file_path = input("\nENTER THE FILE PATH: ")

try:
    with open('marathi_dataset_corrected.txt', 'r', encoding='utf-8') as file:
        translated_lines = []

        for line in file:
            try:
                translated_line = translator.translate(line.strip())
                translated_lines.append(translated_line)
            except Exception as e:
                print("Error translating line:", e)
                translated_lines.append(line)  # Append original line if translation fails

    # output_file_path = input("\nENTER THE OUTPUT FILE PATH: ")
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(translated_lines))

    print("\nTranslation complete. Check the output file.")

except FileNotFoundError:
    print("\nFile not found. Please provide a valid file path.")
except Exception as e:
    print("\nAn error occurred:", e)
