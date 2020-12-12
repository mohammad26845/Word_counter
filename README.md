# Word counter PDF files
---
![commits-since](https://img.shields.io/pypi/pyversions/nltk?style=plastic)
![commits-since](https://img.shields.io/github/commits-since/mohammad26845/Word_counter/V1.0?style=plastic)



A program for counting the number of words(word tokenize) in PDF files.

**It should be noted that this program does not detect scanned files.**

## How to run
To run this file; Just use steps below:

+ Install `python3`, `pip`, `PyPDF2`, `nltk`.
+ Clone the project <a href='https://github.com/mohammad26845/Word_counter.git'>Word_counter</a>

## Table Of Contents
- [NLTK library to identify stopwords](/corpora)
    + About stopwords <a href='https://www.nltk.org/book/ch02.html'>Read more...</a>
- [NLTK library to word tokenize](/tokenizers)
    + About word tokenize <a href='https://www.nltk.org/api/nltk.tokenize.html'>Read more...</a>
- [Sample input file](test.pdf)
- [Sample program output](out.csv)
    

## Tip
NLTK libraries are required.

If you want to install them on your system
You `must` run the following code:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Parameters
You must modify the `filename` variable to rename the input file:
```python
filename = 'Your_file.pdf'
```

To change the number of output words, you must modify the variable `count_word`:
```python
count_word = 30
```


## TODO List
- [x] Create a CSV file
- [ ] Create a Wordclouds
