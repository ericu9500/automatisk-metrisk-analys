import os

def count_lines_and_syllables_in_folder(folder_path):
    total_lines = 0
    total_long_syllables = 0
    total_short_syllables = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                line_count = 0
                long_syllables = 0
                short_syllables = 0
                
                for line in f:
                    line_count += 1
                    long_syllables += line.count('-')
                    short_syllables += line.count('u')
                
                print(f"{filename}: {line_count} rader, {long_syllables} långa stavelser, {short_syllables} korta stavelser")
                
                total_lines += line_count
                total_long_syllables += long_syllables
                total_short_syllables += short_syllables
    
    print(f"Totalt antal rader: {total_lines}")
    print(f"Totalt antal långa stavelser: {total_long_syllables}")
    print(f"Totalt antal korta stavelser: {total_short_syllables}")
    print(f"Totalt antal stavelser: {total_long_syllables + total_short_syllables}")

if __name__ == '__main__':
    folder_path = "hypotactic_txts_greek"
    count_lines_and_syllables_in_folder(folder_path)
