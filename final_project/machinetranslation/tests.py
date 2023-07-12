'''Unit Tests for translation'''

import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    '''Test English to French translation'''
    def test1(self):
        '''Equal Test for boy and Hello'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('boy'), 'garçon')

    def test2(self):
        '''Negative tests'''
        self.assertNotEqual(english_to_french('Hello'), 'Hola')
        self.assertNotEqual(english_to_french('boy'), 'nina')
    
class testFrenchToEnglish(unittest.TestCase):
    '''Test French to English translation'''
    def test1(self):
        '''Test for garçon and Bonjour'''
        self.assertEqual(french_to_english('garçon'), 'boy')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test2(self):
        '''Negative tests'''
        self.assertNotEqual(french_to_english('garçon'), 'girl')
        self.assertNotEqual(french_to_english('Bonjour'), 'human')

unittest.main()
