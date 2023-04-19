#Group names     : Tarek Chaalan, Nick Haga and Zhengyao Huang
#Assignment      : No.3_2
#Due date        : Thursday February 16, 2023

# CFG
grammar = {
    "S": {"aS", "bB", "cC"},
    "B": {"bB", "aC", "cD", ""},
    "C": {"aS", "bD", "cD", ""},
    "D": {"bD", "aB", "cC"},
}

non_terminals = set(grammar.keys())

def parse(s, i, symbol):
    if i == len(s):
        return symbol == ""
    
    if symbol in non_terminals:
        for rule in grammar[symbol]:
            if parse(s, i, rule):
                return True
    else:
        return s[i] == symbol and parse(s, i+1, "")

    return False

# user input
def get_input():
    return input("Enter a string ('q' to quit): ").strip()

while True:
    input_string = get_input()

    if input_string.lower() == 'q':
        break

    if not input_string.endswith("$"):
        print("Invalid input, must end in $")
        continue

    if parse(input_string, 0, "S"):
        print("Accepted")
    else:
        print("Rejected")