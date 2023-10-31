import os
import re

# Initialize variables to keep track of longest and shortest lines
longest_line = 0
shortest_line = float('inf')
longest_file = ""
shortest_file = ""
longest_line_number = 0
shortest_line_number = 0
longest_line_content = ""
shortest_line_content = ""

# Regular expression for extracting Greek text and metrical info between square brackets
regex = re.compile(r'\[(.*?)\], \[(.*?)\]')

# Walk through the 'hypotactic_txts_greek' directory and read all .txt files
for root, dirs, files in os.walk("hypotactic_txts_greek"):
    for file in files:
        if file.endswith(".txt"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for idx, line in enumerate(lines):
                    matches = regex.search(line)
                    if matches:
                        greek_text = matches.group(1)
                        metric_info = matches.group(2)
                        
                        # Check for empty brackets
                        if greek_text.strip() == '':
                            print(f"Empty Greek text in line {idx + 1} of {file}")

                        # Check for suspicious Greek words with more than 20 characters
                        for word in greek_text.split():
                            if len(word) > 20:
                                print(f"Suspicious long word in line {idx + 1} of {file}: {word}")

                        greek_length = len(greek_text)

                        # Update longest line info
                        if greek_length > longest_line:
                            longest_line = greek_length
                            longest_file = file
                            longest_line_number = idx + 1
                            longest_line_content = greek_text

                        # Update shortest line info
                        if greek_length < shortest_line:
                            shortest_line = greek_length
                            shortest_file = file
                            shortest_line_number = idx + 1
                            shortest_line_content = greek_text
                    else:
                        print(f"Line {idx + 1} in {file} does not match the expected format: {line.strip()}")

print(f"The longest Greek line has {longest_line} characters, which is line number {longest_line_number} in {longest_file}: {longest_line_content}")
print(f"The shortest Greek line has {shortest_line} characters, which is line number {shortest_line_number} in {shortest_file}: {shortest_line_content}")
