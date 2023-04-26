from googletrans import Translator

translator = Translator()
# text = "Hello, how are you?"
# translated = translator.translate(text, src="en", dest="vi")
# print(translated.text)

def translate(text, src, dest):
    translated = translator.translate(text, src=src, dest=dest)
    return translated.text


# text = "Hello, how are you?"

# print(translate(text, "en", "vi"))
