'''
Module for translator functions
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Function for English to French translation
    """
    french_text = MyMemoryTranslator('en-GB', 'fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Function for French to English translation
    """
    english_text = MyMemoryTranslator('fr-FR', 'en-GB').translate(french_text)
    return english_text
