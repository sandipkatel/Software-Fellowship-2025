# string_utils.py
def capitalize_words(text):
    """Capitalize each word in a string"""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]