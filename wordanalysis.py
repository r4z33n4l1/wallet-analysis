import json

def create_substring_dictionary():
    count_dictionary = {}
    
    # Read final.txt
    with open('final.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if not word:  # Skip empty lines
                continue
            
            # Split by spaces to handle each word separately
            words = word.split()
            
            # Process each word individually
            for single_word in words:
                # Get all possible substrings of length 1 or more
                word_length = len(single_word)
                for start in range(word_length):
                    for length in range(1, word_length - start + 1):
                        # Convert substring to lowercase before adding to dictionary
                        substring = single_word[start:start + length].strip().lower()
                        
                        # Skip substrings that are just spaces or special characters
                        if not substring or substring.isspace() or substring in ['.', '-', '_']:
                            continue
                        
                        # Add to dictionary with count
                        if substring in count_dictionary:
                            count_dictionary[substring] += 1
                        else:
                            count_dictionary[substring] = 1
    
    # Save dictionary to JSON file
    with open('substrings.json', 'w', encoding='utf-8') as f:
        json.dump(count_dictionary, f, indent=4, sort_keys=True)
    
    print(f"Found {len(count_dictionary)} unique substrings")
    return count_dictionary

def sort_and_filter_dictionary():
    # Read the original JSON file
    with open('substrings.json', 'r', encoding='utf-8') as f:
        count_dictionary = json.load(f)
    
    # Filter out single-character substrings and sort by count
    filtered_dict = {k: v for k, v in count_dictionary.items() if len(k) >= 3 and v > 2}
    sorted_dict = dict(sorted(filtered_dict.items(), key=lambda x: x[1], reverse=True))
    
    # Save sorted dictionary to new JSON file
    with open('sorted_substrings.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_dict, f, indent=4)
    
    print(f"Saved {len(sorted_dict)} substrings (length >= 2) to sorted_substrings.json")
    return sorted_dict

if __name__ == "__main__":
    substring_dict = create_substring_dictionary()
    sorted_dict = sort_and_filter_dictionary()
