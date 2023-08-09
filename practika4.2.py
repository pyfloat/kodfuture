import re

def check_simbols(k): 
    numbers = "[0-9]" 
    t = re.findall(numbers, k) 
    if len(t) == 0:
        print("В тексте нет цифр")
    else:
        print(f"Найденные цифры в тексте: {t}")
        return t
    
k = input("Напишите текст для проверки: ")
check_simbols(k)
