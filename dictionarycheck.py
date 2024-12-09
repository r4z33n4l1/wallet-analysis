import json

def load_english_dictionary():
    # Load the words_dictionary.json file
    with open('words_dictionary.json', 'r') as f:
        english_words = json.load(f)
    return english_words

def find_english_words_in_wallets():
    english_words = load_english_dictionary()
    wallet_words = {}
    word_occurrences = {}
    
    # Read final.txt
    with open('final.txt', 'r') as f:
        for line in f:
            wallet_name = line.strip()
            if not wallet_name:  # Skip empty lines
                continue
            
            # Set to store unique valid English words found in the wallet name
            valid_words = set()
            
            # Split by spaces to handle each word separately
            words = wallet_name.split()
            
            # Process each word individually
            for single_word in words:
                # Get all possible substrings of length 2 or more
                word_length = len(single_word)
                for start in range(word_length):
                    for length in range(2, word_length - start + 1):
                        substring = single_word[start:start + length].strip().lower()
                        # if subtr
                        
                        # Check if the substring is a valid English word
                        if len(substring) > 2 and substring in english_words:
                            valid_words.add(substring)
                            # Count occurrences of each valid word
                            if substring in word_occurrences:
                                word_occurrences[substring] += 1
                            else:
                                word_occurrences[substring] = 1
            
            # Only add to dictionary if we found valid words
            if valid_words:
                wallet_words[wallet_name] = sorted(list(valid_words))
    
    # Save the wallet words dictionary to a JSON file
    with open('wallet_english_words.json', 'w', encoding='utf-8') as f:
        json.dump(wallet_words, f, indent=4, sort_keys=True)
    
    # sort word_occurrences by value
    word_occurrences = dict(sorted(word_occurrences.items(), key=lambda item: item[1], reverse=True))
    # Save the word occurrences dictionary to a separate JSON file
    with open('word_occurrences.json', 'w', encoding='utf-8') as f:
        json.dump(word_occurrences, f, indent=4)
    
    print(f"Found English words in {len(wallet_words)} wallet names")
    print(f"Recorded {len(word_occurrences)} unique English words")
    return wallet_words, word_occurrences

if __name__ == "__main__":
    wallet_words, word_occurrences = find_english_words_in_wallets() 