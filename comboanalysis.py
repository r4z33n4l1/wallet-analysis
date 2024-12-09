import json
from collections import defaultdict

def analyze_combinations():
    # Load the word_combinations.json file
    with open('word_combinations.json', 'r') as f:
        combinations = json.load(f)
    
    # Create a nested dictionary using defaultdict
    length_sorted = defaultdict(dict)
    
    # Go through each wallet and its combinations
    for wallet_name, combos in combinations.items():
        # Get the length of first tuple (assuming all tuples for a wallet have same length)
        if combos:  # Check if there are any combinations
            combo_length = len(combos[0])
            length_sorted[combo_length][wallet_name] = combos
    
    # Convert defaultdict to regular dict for JSON serialization
    # Also sort by combo length
    sorted_dict = {}
    for length in sorted(length_sorted.keys()):
        # Sort the inner dictionary by wallet name
        sorted_dict[str(length)] = dict(sorted(length_sorted[length].items()))
    
    # Save to new JSON file
    with open('length_sorted_combinations.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_dict, f, indent=4)
    
    print(f"Sorted combinations by {len(sorted_dict)} different lengths")
    # Print summary of how many wallets in each length category
    for length, wallets in sorted_dict.items():
        print(f"Length {length}: {len(wallets)} wallets")
    
    return sorted_dict

if __name__ == "__main__":
    sorted_combinations = analyze_combinations()
