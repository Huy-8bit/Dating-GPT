from googletrans import Translator

translator = Translator()


def translate(text, src, dest):
    translated = translator.translate(text, src=src, dest=dest)
    return translated.text


