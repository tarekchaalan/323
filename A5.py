#Group names     : Tarek Chaalan, Nick Haga and Zhengyao Huang
#Assignment      : No.5
#Due date        : Thursday March 2, 2023

with open("A5.txt", "r") as h5, open("newA5.txt", "w") as newh5:
    for line in h5:

        # remove specific line
        if line.startswith("                   "):
            continue

        # Extract leading whitespaces from the line
        ws = line[:len(line)-len(line.lstrip())]

        # Remove anything that comes after **
        line = line.split("**")[0].strip()
        
        # Remove blank lines
        if not line:
            continue
        
        # Split the line into words, and join them back with a single space
        words = line.split()
        line = " ".join([word.strip() for word in words])
        
        # Write updated lines to new file, and add the leading whitespaces 
        # so they have the same leading whitespaces as the input file
        newh5.write(ws + line + "\n")

# Print input file
with open('A5.txt', 'r') as f:
    print("\nA5.txt:\n")
    print(f.read())

# Print output file
with open('newA5.txt', 'r') as f:
    print("newA5.txt:\n")
    print(f.read())