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

"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
# Prompt for file name
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

words_list = []  # List to store unique words

# Read file line by line
for line in fhand:
    words = line.split()  # Split line into words
    for word in words:
        if word not in words_list:
            words_list.append(word)  # Add only unique words

words_list.sort()  # Sort list in alphabetical order
print(words_list)

""""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
# Prompt for file name
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0  # Initialize count

# Read file line by line
for line in fhand:
    if line.startswith('From '):  # Check if line starts with 'From ' (not 'From:')
        words = line.split()  # Split the line into words
        print(words[1])  # Print the email address (second word)
        count += 1  # Increment count

# Print total count
print("There were", count, "lines in the file with From as the first word")


"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
# Prompt for file name
filename = input("Enter file name: ")
try:
    file = open(filename, "r")
except:
    print("File cannot be opened:", filename)
    quit()

# Dictionary to store email counts
email_counts = {}

# Read file line by line
for line in file:
    if line.startswith("From "):  # Only consider lines that start with 'From '
        words = line.split()
        if len(words) > 1:  # Ensure there is an email in the line
            email = words[1]  # The second word is the sender's email
            email_counts[email] = email_counts.get(email, 0) + 1  # Count occurrences

# Find the most prolific sender
max_email = max(email_counts, key=email_counts.get)
max_count = email_counts[max_email]

print(max_email, max_count)




"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
# Abrir el archivo
file_name = "mbox-short.txt"
handle = open(file_name)

# Diccionario para almacenar los conteos de cada hora
hour_counts = {}

# Leer el archivo línea por línea
for line in handle:
    if line.startswith("From "):  # Filtra solo las líneas que comienzan con "From "
        words = line.split()  
        time = words[5]  # Extrae la parte de la hora (formato HH:MM:SS)
        hour = time.split(":")[0]  # Obtiene solo la hora (HH)
        
        # Incrementa el contador para esa hora
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Ordenar los resultados por hora
sorted_hours = sorted(hour_counts.items())

# Imprimir el resultado final
for hour, count in sorted_hours:
    print(hour, count)


