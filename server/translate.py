from googletrans import Translator

translator = Translator()
text = "Hello, how are you?"
translated = translator.translate(text, src="en", dest="vi")
print(translated.text)
