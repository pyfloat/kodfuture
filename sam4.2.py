import re

def check_symbols(value): 
    symbols_pattern = r"[<>,*&^%$#@!-=+'0-9]" 
    symbols_found = re.findall(symbols_pattern, value) 
    if len(symbols_found) == 0:
        print("Добавьте несколько символов или цифр")
        return False
    else:
        return True
    
def validate_password(value): 
    password_length = len(value) # 
    if password_length > 6 and check_symbols(value): 
        print("Ваш пароль верен!")
    else:
        print("Ваш пароль недостаточно хорош...")

value = input('Введите пароль для проверки: ')
validate_password(value)
