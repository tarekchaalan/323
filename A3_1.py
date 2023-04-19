#Group names     : Tarek Chaalan, Nick Haga and Zhengyao Huang
#Assignment      : No.3_1
#Due date        : Thursday February 16, 2023

reserved = ["while", "for", "switch", "do", "return"]

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_identifier(token):
    if token[0].isalpha() or token[0] == '_':
        for char in token[1:]:
            if not char.isalnum() and char != '_':
                return False
        return True
    else:
        return False

with open("A3_token.txt", "r") as f:
    tokens = f.read().split()

print("Token".ljust(15), "number".ljust(10), "identifier".ljust(10), "reserved word")

for token in tokens:
    is_num = "yes" if is_number(token) else "no"
    is_id = "yes" if is_identifier(token) else "no"
    is_res = "yes" if token in reserved else "no"
    print(token.ljust(15), is_num.ljust(10), is_id.ljust(10), is_res)