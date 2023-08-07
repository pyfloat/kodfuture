from captcha.image import ImageCaptcha 
import random

def generate_cap_text():
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    code = ""
    for i in range(7):
        code += random.choice(letters)
    return code

cap = ImageCaptcha(width= 150, height= 150) 
cap = cap.create_captcha_image(generate_cap_text(), color='red', background='white')
cap.show() 