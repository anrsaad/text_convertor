from googletrans import Translator

def translate_to_arabic(text):
    translator = Translator()
    translation = translator.translate(text, dest='fr')
    return translation.text

# Example usage
while True :
    
    
    english_text = input(str("type text to convert here : "))
    if english_text == "quit":
        break
    text = translate_to_arabic(english_text)
    print(text)

