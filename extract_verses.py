from bs4 import BeautifulSoup
import os

# Check if the source folder exists
source_folder = "hypotactic_htmls_greek"
if not os.path.exists(source_folder):
    print(f"Source folder {source_folder} does not exist. Exiting.")
    exit()

# Create the target folder if it doesn't exist
target_folder = "hypotactic_txts_greek"
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Iterate over each .html file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.html'):
        filepath = os.path.join(source_folder, filename)
        
        print(f"Processing {filename}...")

        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        lines = soup.find_all('div', {'class': 'line'})

        # Create .txt file for the output
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_filepath = os.path.join(target_folder, txt_filename)
        
        # Open .txt file to write the parsed content
        with open(txt_filepath, 'w', encoding='utf-8') as txt_f:
            for line in lines:
                sentence = ''
                syll_pattern = ''
                words = line.find_all('span', {'class': 'word'})
    
                for word in words:
                    word_text = ''.join(syllable.get_text().strip() for syllable in word.find_all('span'))
                    word_pattern = ''.join('-' if syllable.get('class') and 'long' in syllable['class'] else 'u' for syllable in word.find_all('span'))

                    sentence += word_text + ' '
                    syll_pattern += word_pattern + ' '

    
                txt_f.write(f"[{sentence.strip()}], [{syll_pattern.strip()}]\n")

print("Done.")
