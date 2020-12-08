import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import csv

# Write a for-loop to open many files (leave a comment if you'd like to learn how).
filename = 'test.pdf'

# Count of output file
count_word = 30

# open allows you to read the file.
pdfFileObj = open(filename, 'rb')

# The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Discerning the number of pages will allow us to parse through all the pages.
num_pages = pdfReader.numPages
count = 0
text = ""
# The while loop will read each page.
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

# The word_tokenize() function will break our text phrases into individual words.
tokens = word_tokenize(text)

# Remove single-character tokens (mostly punctuation)
tokens = [word for word in tokens if len(word) > 1]

# Remove numbers
tokens = [word for word in tokens if not word.isnumeric()]

# We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(', ')', ';', ':', '[', ']', ',', '.']

# We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much
# value as keywords.

stop_words = stopwords.words('english')

# We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word.lower() in stop_words and not word in punctuations]

# A frequency distribution for the outcomes of an experiment.
f_dist = FreqDist()
for word in keywords:
    f_dist[word.lower()] += 1

# Create and write a csv file
with open('out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["word", "weight"])
    writer.writerows(f_dist.most_common(count_word))

# Print all of data
print(f_dist.most_common(count_word))


