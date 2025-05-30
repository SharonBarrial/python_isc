"""
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2202494.json (Sum ends with 92)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at xml3.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
Turning in the Assignment

Enter the sum from the actual data and your Python code below:
Sum: 
 (ends with 92)

 """
import urllib.request
import json

# Pedir URL
url = input("Enter location: ")
print(f"Retrieving {url}")

# Leer datos desde la URL
data = urllib.request.urlopen(url).read()
print(f"Retrieved {len(data)} characters")

# Parsear JSON
info = json.loads(data)

# Extraer y sumar los valores de 'count'
comments = info["comments"]
print("Count:", len(comments))

total = sum(comment["count"] for comment in comments)
print("Sum:", total)
