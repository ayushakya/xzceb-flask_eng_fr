'''Unit Tests for translation'''

import unittest
from machinetranslation.translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    '''Test English to French translation'''
    def test1(self):
        '''Test for boy and Hello'''
        self.assertEqual(english_to_french('boy'), 'garçon')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    
class testFrenchToEnglish(unittest.TestCase):
    '''Test French to English translation'''
    def test1(self):
        '''Test for garçon and Bonjour'''
        self.assertEqual(french_to_english('garçon'), 'boy')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
