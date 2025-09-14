#!/usr/bin/env python3
import sys
from howlongtobeatpy import HowLongToBeat

def get_max_lengths(data):
    # Get the maximum length of each column
    max_lengths = [len(str(cell)) for cell in data[0]]
    for row in data[1:]:
        for i, cell in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(cell)))
    return max_lengths

def print_dynamic_table(data):
    # Calculate column widths
    max_lengths = get_max_lengths(data)
    
    # Print header
    print("+" + "+".join("-" * (width + 2) for width in max_lengths) + "+")
    
    # Print header row
    header = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(data[0], max_lengths)) + " |"
    print(header)
    
    # Print separator
    print("+" + "+".join("-" * (width + 2) for width in max_lengths) + "+")
    
    # Print data rows
    for row in data[1:]:
        formatted_row = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(row, max_lengths)) + " |"
        print(formatted_row)
    
    # Print bottom border
    print("+" + "+".join("-" * (width + 2) for width in max_lengths) + "+")


search_term = " ".join(sys.argv[1:])

results = HowLongToBeat().search(search_term)

data =[["Title", "Main Story", "Main+Extra", "Completionist"]]
for result in results:
    data.append([f"\x1b]8;;{result.game_web_link}\x1b\\{result.game_name}\x1b]8;;\x1b\\", f"{int(result.main_story)}h {round(result.main_story%1*60)}m", f"{int(result.main_extra)}h {round(result.main_extra%1*60)}m", f"{int(result.completionist)}h {round(result.completionist%1*60)}m"])
print_dynamic_table(data)
