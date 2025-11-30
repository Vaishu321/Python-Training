
# Read products.txt and write catalog.txt with aligned columns

# Read all lines from products.txt
with open('products.txt', 'r') as infile:
    lines = infile.readlines()

# Prepare output
with open('catalog.txt', 'w') as outfile:
    outfile.write("Product     Price\n")  # Header
    for line in lines:
        name, price = line.strip().split()
        outfile.write(f"{name:<12}{price}\n")  # Left-align name, keep price






