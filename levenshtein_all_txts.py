from functools import lru_cache
import os

def lev_dist(a, b):
    @lru_cache(None)  # for memorization
    def min_dist(s1, s2):
        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)
        return 1 + min(
            min_dist(s1, s2 + 1),      # insert character
            min_dist(s1 + 1, s2),      # delete character
            min_dist(s1 + 1, s2 + 1),  # replace character
        )
    return min_dist(0, 0)

def find_closest_patterns(input_pattern, folder_path="hypotactic_txts_greek"):
    # Initialize a list to store (distance, line) pairs
    distances = []
    
    # Loop through the files in the folder
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), 'r') as f:
            for line in f:
                # Extract the u and - pattern from the line and remove spaces
                pattern = line.strip().split("], [")[1][:-1].replace(" ", "")
                
                # Calculate the Levenshtein distance
                distance = lev_dist(input_pattern, pattern)
                
                # Add the (distance, line) pair to the list
                distances.append((distance, line.strip()))
                
    # Sort the list by distance
    distances.sort(key=lambda x: x[0])
    
    # Print the 10 closest lines
    for i, (distance, line) in enumerate(distances[:10]):
        print(f"Rank {i+1}, Distance: {distance}, Line: {line}")

if __name__ == "__main__":
    # Example usage
    input_pattern = "u--uuu-"  # Replace this with your actual input
    find_closest_patterns(input_pattern)
