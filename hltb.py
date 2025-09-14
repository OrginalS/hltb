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

def print_dynamic_table(data, links):

    GRAY = '\x1b[90m'
    RESET = '\x1b[0m'

    # Calculate column widths
    max_lengths = get_max_lengths(data)

    # Print header
    print(GRAY + "+" + "+".join("-" * (width + 2) for width in max_lengths) + "+" + RESET)

    # Print header row
    header = f"{GRAY}| {RESET}" + f"{GRAY} | {RESET}".join(str(cell).ljust(width) for cell, width in zip(data[0], max_lengths)) + f"{GRAY} |{RESET}"
    print(header)

    # Print separator
    print(GRAY + "+" + "+".join("-" * (width + 2) for width in max_lengths) + "+" + RESET)

    # Print data rows
    for idx, row in enumerate(data[1:], start=1):
        # First column with link
        first_col = f'\x1b]8;;{links[idx-1]}\x1b\\{row[0].ljust(max_lengths[0])}\x1b]8;;\x1b\\'

        # Format remaining columns normally
        remaining_cols = f"{GRAY} | {RESET}".join(str(cell).ljust(width) for cell, width in zip(row[1:], max_lengths[1:]))

        # Combine first column with remaining columns
        formatted_row = f"{GRAY}|{RESET} {first_col} {GRAY}|{RESET} {remaining_cols} {GRAY}|{RESET}"
        print(formatted_row)

    # Print bottom border
    print(GRAY + "+" + "+".join("-" * (width + 2) for width in max_lengths) + "+" + RESET)

# Main program
search_term = " ".join(sys.argv[1:])
results = HowLongToBeat().search(search_term)

data =[["Title", "Main Story", "Main+Extra", "Completionist"]]
links = []

for result in results:
    data.append([
        result.game_name,
        f"{int(result.main_story)}h {round(result.main_story%1*60)}m",
        f"{int(result.main_extra)}h {round(result.main_extra%1*60)}m",
        f"{int(result.completionist)}h {round(result.completionist%1*60)}m"
    ])
    links.append(result.game_web_link)

print_dynamic_table(data, links)
