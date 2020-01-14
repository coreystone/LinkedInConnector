# LinkedInConnector
A tool to facilitate corporate outreach and connect with potential Mergers &amp; Acquisitions clientele in the industry,
increasing principals' connections and presence on LinkedIn.


## Introduction
This is a Python program and GUI I developed to solve a repetitive problem I identified at work: combing through a CSV file,
with up to thousands of rows, and manually copying and pasting cells to search online. Previously, the User would have to 
look manually go row-by-row through a CSV of contacts, manually searching for each person, create a message to send to them,
and finally mark if they were found or not on the CSV file. 

![alt text](https://github.com/coreystone/LinkedInConnector/blob/master/RedactedPreview.PNG "")

This program alleviates this struggle by automatically parsing each row and displaying it in an easily consumed GUI,
with functional buttons to manipulate the CSV, search for contacts, and generate messages for them in the click of a button.

## Walkthrough
![alt text](https://github.com/coreystone/LinkedInConnector/blob/master/Walkthrough.png "")

## Libraries
* To parse the CSV file full of hundreds to thousands of contacts, I used the [**csv**](https://docs.python.org/3/library/csv.html) Python libarary.
* To deal with all of this data, the [**pandas**](https://pandas.pydata.org/) libarary helped to form and manipulate tables.
* To encapsulate the program into a GUI, I used [**PyQt5**](https://pypi.org/project/PyQt5/), allowing me to create Windows Forms. This allowed me to make something that could be used by others in the office with little to no hassle. 

