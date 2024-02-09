import re

# Example of using re.match() to find a pattern at the beginning of a string
pattern = r'^Hello'
text = 'Hello, World!'
match = re.match(pattern, text)
if match:
    print("Pattern matched at the beginning of the string.")

# Example of using re.findall() to extract all occurrences of a pattern in a string
pattern = r'\b\w{4}\b'  # Match 4-letter words
text = 'This is a simple example demonstrating regular expressions in Python.'
matches = re.findall(pattern, text)
print("Four-letter words in the text:", matches)




# Example of old-style string formatting using %
name = 'Alice'
age = 30
print("Name: %s, Age: %d" % (name, age))

# Example of using str.format() method
print("Name: {}, Age: {}".format(name, age))

# Example of using f-strings (Formatted String Literals)
print(f"Name: {name}, Age: {age}")


# Example of encoding and decoding Unicode strings
text = 'Hello, 你好'
encoded_text = text.encode('utf-8')  # Encode Unicode string to bytes using UTF-8 encoding
print("Encoded text:", encoded_text)

decoded_text = encoded_text.decode('utf-8')  # Decode bytes to Unicode string using UTF-8 encoding
print("Decoded text:", decoded_text)


# Example of using string methods for searching and manipulation
text = '   Hello, World!   '
print("Original string:", text)
print("Stripped string:", text.strip())
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replaced string:", text.replace('Hello', 'Hi'))

