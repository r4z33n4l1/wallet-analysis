import json
from itertools import combinations
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('wordcombo.log'),
        logging.StreamHandler()  # This will print to console as well
    ]
)

def find_word_combinations():
    # Load the wallet_english_words.json file
    with open('wallet_english_words.json', 'r') as f:
        wallet_words = json.load(f)
    
    word_combinations = {}
    total_wallets = len(wallet_words)
    
    logging.info(f"Starting to process {total_wallets} wallet names")
    
    for idx, (wallet_name, word_list) in enumerate(wallet_words.items(), 1):
        # Log progress every wallet
        logging.info(f"Processing wallet {idx}/{total_wallets}: {wallet_name}")
        
        # Convert wallet name to lowercase for comparison
        wallet_lower = wallet_name.lower().replace(' ', '')
        valid_combos = set()
        
        # First check if any single word matches the entire name
        for word in word_list:
            if word.lower() == wallet_lower:
                valid_combos.add((word,))
        
        # Then try combinations of multiple words
        for combo_length in range(2, len(word_list) + 1):
            # Log when trying new combination length
            logging.debug(f"Trying combinations of length {combo_length} for {wallet_name}")
            
            # Get all possible combinations of the given length
            for combo in combinations(word_list, combo_length):
                # Sort words by their position in the original wallet name
                sorted_combo = sorted(combo, key=lambda x: wallet_lower.find(x))
                
                # Check if concatenated words make the original name
                if ''.join(sorted_combo) == wallet_lower:
                    valid_combos.add(tuple(sorted_combo))
        
        # Only add to dictionary if we found valid combinations
        if valid_combos:
            word_combinations[wallet_name] = sorted(list(valid_combos))
            logging.info(f"Found {len(valid_combos)} valid combinations for {wallet_name}")
    
    # Save the combinations to a JSON file
    with open('word_combinations.json', 'w', encoding='utf-8') as f:
        json.dump(word_combinations, f, indent=4, sort_keys=True)
    
    logging.info(f"Completed processing. Found word combinations for {len(word_combinations)} wallet names")
    return word_combinations

if __name__ == "__main__":
    logging.info("Starting word combination analysis")
    combinations_dict = find_word_combinations()
    logging.info("Analysis complete")
