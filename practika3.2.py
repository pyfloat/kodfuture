import random 

def generate_cap_text():
    letters = "1234567890"
    code = "" 
    for i in range(5): 
        code += random.choice(letters)
    return code

print(generate_cap_text()) 