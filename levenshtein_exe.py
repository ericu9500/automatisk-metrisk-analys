#!/usr/bin/env python3

import os
import argparse
from functools import lru_cache

def lev_dist(a, b):
    @lru_cache(None)
    def min_dist(s1, s2):
        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)
        return 1 + min(
            min_dist(s1, s2 + 1),
            min_dist(s1 + 1, s2),
            min_dist(s1 + 1, s2 + 1),
        )
    return min_dist(0, 0)

def find_closest_patterns(input_pattern, folder_path):
    distances = []
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), 'r') as f:
            for line_number, line in enumerate(f, 1):
                pattern = line.strip().split("], [")[1][:-1].replace(" ", "")
                distance = lev_dist(input_pattern, pattern)
                distances.append((distance, line.strip(), file_name, line_number))
    distances.sort(key=lambda x: x[0])
    for i, (distance, line, file_name, line_number) in enumerate(distances[:10]):
        print(f"Rank {i+1}, Distance: {distance}, Line: {line}, Source: Line {line_number} in {file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find closest u and - patterns in a folder of text files.')
    parser.add_argument('input_pattern', type=str, help='The u and - pattern to compare.')
    parser.add_argument('--folder_path', type=str, default="hypotactic_txts_greek", help='Path to the folder containing the text files.')
    
    args = parser.parse_args()
    find_closest_patterns(args.input_pattern, args.folder_path)
