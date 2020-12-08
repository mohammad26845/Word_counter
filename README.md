# Word counter PDF files

A program for counting the number of words(word tokenize) in PDF files.

**It should be noted that this program does not detect scanned files.**

##Installation
You must have the following libraries installed before running:
+ PyPDF2
+ nltk


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