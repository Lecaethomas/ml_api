# Machine Learning API
## How?
Install the requirements.txt
### Then what's going on?
The API takes text as input and then applies few preprocessing : 
- removal of stop-words/punctuation/non-alphabetic characters
- lemmatisation 
- vectorisation using tf-idf
and then infers the note using the preprocessed text and the model built using SVM algorithm.
This note is then returned by the API
### The interface 😂
To test the API you can use the very simple interface made in few minutes using streamlit
![Enter a comment](/supports/Screenshot_1.png)
![Get the note](/supports/Screenshot_2.png)
