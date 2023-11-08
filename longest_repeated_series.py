import os
import re

# Function to find the longest sequence of a character in a string
def find_longest_sequence(sequence, character):
    return max(re.findall(f"{character}+", sequence), key=len, default="")

# Directory path where the txt files are located
folder_path = "hypotactic_txts_greek"

# Lists to store the longest sequences
longest_u_sequences = []
longest_dash_sequences = []

# Process each file in the directory
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file:
                line_number += 1
                try:
                    _, metrical_pattern = line.strip().split('], [')
                    metrical_pattern = metrical_pattern.replace(" ", "").replace("]", "")

                    # Find the longest sequence of 'u' and '-'
                    longest_u = find_longest_sequence(metrical_pattern, 'u')
                    longest_dash = find_longest_sequence(metrical_pattern, '-')

                    # Store the sequences along with file name and line number
                    longest_u_sequences.append((len(longest_u), longest_u, file_name, line_number))
                    longest_dash_sequences.append((len(longest_dash), longest_dash, file_name, line_number))

                except ValueError:
                    print(f"Line in file {file_name} not in expected format on line {line_number}: {line}")

# Sort and get the top 100
longest_u_sequences.sort(reverse=True)
longest_dash_sequences.sort(reverse=True)
top_100_u_sequences = longest_u_sequences[:100]
top_100_dash_sequences = longest_dash_sequences[:100]

# Save to a .txt file with the same name as the script
script_name = os.path.basename(__file__).split('.')[0]
output_filename = f"{script_name}_longest_sequences.txt"

with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write("Top 100 lines with the longest 'u' sequences:\n")
    for length, sequence, file, line_number in top_100_u_sequences:
        output_file.write(f"{sequence} (Length: {length}) in file: {file}, line: {line_number}\n")
    
    output_file.write("\nTop 100 lines with the longest '-' sequences:\n")
    for length, sequence, file, line_number in top_100_dash_sequences:
        output_file.write(f"{sequence} (Length: {length}) in file: {file}, line: {line_number}\n")

print(f"Results saved to {output_filename}")
