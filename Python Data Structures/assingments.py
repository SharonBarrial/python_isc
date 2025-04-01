"""
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
"""
text = "X-DSPAM-Confidence: 0.8475"

# Find the position of the colon
colon_pos = text.find(':')

# Extract the number using slicing
number_str = text[colon_pos + 1:].strip()

# Convert to float
number = float(number_str)

# Print the result
print(number)


