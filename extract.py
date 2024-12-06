import re
from bs4 import BeautifulSoup

def extract_wallet_names(html_content):
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <a> tags within the first td of each row
    wallet_elements = soup.select('tr td:first-child a')
    
    # Extract unique wallet names
    wallet_names = set()
    for element in wallet_elements:
        wallet_names.add(element.text.strip())
    
    # Write wallet names to file
    with open('wallet_names2.txt', 'w') as f:
        for name in sorted(wallet_names):
            f.write(name + '\n')

def combine_wallet_names():
    # Set to store unique wallet names
    unique_names = set()
    
    # Read wallet_names.txt and add to set
    try:
        with open('wallet_names.txt', 'r') as f:
            for line in f:
                name = line.strip()
                if name:  # Only add non-empty lines
                    unique_names.add(name)
    except FileNotFoundError:
        print("Warning: wallet_names.txt not found")
    
    # Write unique names to final.txt
    with open('final.txt', 'w') as f:
        for name in sorted(unique_names):
            f.write(name + '\n')
    
    print(f"Found {len(unique_names)} unique wallet names")

# Read HTML file
with open('name2.html', 'r') as f:
    html_content = f.read()

# Extract wallet names
extract_wallet_names(html_content)

# Add this to the end of your script
if __name__ == "__main__":
    # Then combine and deduplicate
    combine_wallet_names()
