# main.py
from math_utils import add, calculate_area
from string_utils import capitalize_words

result = add(5, 3)
area = calculate_area(10, 5)
formatted_text = capitalize_words("hello world")

print(f"Sum: {result}, Area: {area}, Text: {formatted_text}")