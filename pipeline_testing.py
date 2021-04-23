from transformers import pipeline

translation = pipeline("translation_en_to_de")

while True:
    text = input()
    translated_text = translation(text, max_length=40)[0]['translation_text']
    print(translated_text)
