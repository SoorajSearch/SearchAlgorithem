# SearchAlgorithem
Search Algorithem for SoorajSearch to Search Useful files
# How it works 
There are two types of this algorithm. True or False and File Finder
File Finder finds useful files based on the query by removeing the stopwords in a folder
True or False takes a file content and query to determine if the file is useful or not
# Example
This Example shows you of using True or False
```python
from TrueOrFalse import *
with open(file, 'r') as f:
  content = file.readline() # A cheetah is a animal
  check = searchAlgorithem("What is a cheetah", content) # Returns True
  print(check)
