# Assignment 1: Review Data Analysis and Processing
> CE/CZ4045 Natural Language Processing \
> School of Computer Science and Engineering \
> Nanyang Technological University, Singapore

##  Data

The data folder contains the: 
1. Raw **JSON** data for the reviews.
2. **CSV** data from the json for analysis.

##  Third-Party Libraries 
* nltk : https://www.nltk.org
* pandas : https://pandas.pydata.org
* numpy : https://numpy.org
* tqdm : https://tqdm.github.io
* matplotlib : https://matplotlib.org
* keras : https://keras.io
* spacy : https://spacy.io
* gensim : https://pypi.org/project/gensim
* sumy : https://pypi.org/project/sumy
* transformers : https://huggingface.co/transformers
* sentencepiece : https://pypi.org/project/sentencepiece
* sklearn : https://scikit-learn.org/stable
* jupyter : https://jupyter.org/install

##  Installation 

```console
pip install nltk pandas numpy tqdm matplotlib keras sklearn gensim spacy sumy transformers sentencepiece
```

> Open Terminal (Mac) / Powershell (Windows)

```console
conda activate
jupyer notebook
```

## 1. Dataset Analysis
### 1.1 Tokenization & Stemming
#### Tokenization
1. Navigate to `Jupyter/[1.1] Tokenize.ipynb`
2. Run all the cells.

The output of the tokenization results are saved in the `Results/` folder.
#### Stemming
1. Navigate to `Jupyter/[1.1] Stemming.ipynb`
2. Run all the cells.

### 1.2 POS Tagging

### 1.3 Writing Style
1. Navigate to `Jupyter/[1.3] StackOverflow.ipynb`
2. Run All Cells

### 1.4 Most Frequent Noun-Adj Pairs
1. Navigate to `Jupyter/[1.4] Noun-Adj-Pairs.ipynb`.
2. Run all the cells.

```
1.0  Star Reviews
-------------
[(('time', 'first'), 5), (('reviews', 'good'), 3), (('time', 'second'), 3), (('appointment', 'able'), 3), (('fly', 'dead'), 3), (('service', 'horrible'), 3), (('night', 'last'), 2), (('Charlotte', 'local'), 2), (('food', 'fast'), 2), (('quality', 'poor'), 2)]

2.0  Star Reviews
-------------
...
```

Every review in the dataset is associated with a “star” rating ranging between 1 to 5. 50 reviews are randomly selected (each from a unique business) of rating 1-star and the top 10 most frequently occurring noun-adjective pairs are extracted in the below tables. The process is repeated for 20 reviews with rating 2, 3, 4, and 5 stars respectively.

---

## 2. Indicative Adjective Phrases
1. Navigate to `Jupyter/[2]IndicativeAdjectivePhrases.ipynb`.
2. Run all the cells. 

The last cell of the notebook produces the list of indicative adjective phrases for business b1 with id:j7HO1YeMQGYo3KibMXZ5vg

---

## 3. Summarization Application

Steps to run application:
1. Go to Jupyter folder
2. run application.py 

Enter your review text:
![image](https://user-images.githubusercontent.com/43417744/138554561-24c4801f-b70f-4bf1-b620-d6fd5e8f2c46.png)

Choose your summarizer:

![image](https://user-images.githubusercontent.com/43417744/138554589-2b78da69-aee3-4479-a3ee-52c9407a49fa.png)

Example Result:

![image](https://user-images.githubusercontent.com/43417744/138554635-b0604d04-efdf-4bf9-b3e2-3222f6a4b2cc.png)

----

## Authors

* Tharakan Roham Roy
* Gupta Jay
* Jose Jeswin
* Adrakatti Vivek
* Dandapath Soham


