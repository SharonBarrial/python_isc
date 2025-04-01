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

"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""
# Prompt user for file name
fname = input("Enter file name: ")

try:
    # Open the file
    with open(fname, 'r') as fhand:
        for line in fhand:
            print(line.upper().rstrip())  # Convert to uppercase and remove trailing spaces

except FileNotFoundError:
    print("Error: File not found")

""""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
""""
# Prompt for the file name
fname = input("Enter file name: ")

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
total = 0.0

# Process the file line by line
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        # Find the colon and extract the number after it
        colon_pos = line.find(":")
        number_str = line[colon_pos+1:].strip()
        try:
            number = float(number_str)
            total += number
            count += 1
        except:
            continue

if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines found with X-DSPAM-Confidence:")


