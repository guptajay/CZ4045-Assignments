# CE/CZ4045 Natural Language Processing
> School of Computer Science and Engineering \
> Nanyang Technological University, Singapore

# Assignment 1: Review Data Analysis and Processing

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

We did a brief analysis on the yelp dataset to get familiar with the data. 
The jupyter notebook can be located in `Jupyter/Data Analysis.ipynb`.

### 1.1 Tokenization & Stemming
#### Tokenization
1. Navigate to `Jupyter/[1.1] Tokenize.ipynb`
2. Run all the cells.

The output of the tokenization results are saved in the `Results/` folder.
#### Stemming
1. Navigate to `Jupyter/[1.1] Stemming.ipynb`
2. Run all the cells.

### 1.2 POS Tagging
1. Navigate to `Jupyter/[1.2] POS_tagging.ipynb`
2. Run all the cells.

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
1. Navigate to `Jupyter/[2] IndicativeAdjectivePhrases.ipynb`.
2. Run all the cells. 

The last cell of the notebook produces the list of indicative adjective phrases for business b1 with id: `j7HO1YeMQGYo3KibMXZ5vg`

---

## 3. Summarization Application

### Extractive Summarizer
1. Go to the `Jupyter/[3.1] Extractive Summarizer.ipynb`
2. Run all the cells.

The two packages used for extractive summarizer are gensim and sumy. The corresponding output is below each section

### Abstractive Summarizer
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


# Assignment 2: Deep Learning Based NLP Methods

## Question 1
Only PyTorch-FNN.ipynb must be run to load and preprocess the data as well as train the FNN models and observe the output of the models and the generated text. The results including generated text, plots for model loss and model perplexity are present in Question 1 FNN/results.

### 1.4 Model Training for FNN Model without Shared Weights.
```
--- Training: 1 ---
| epoch   0 |     0/59674 batches | lr 0.002 | ms/batch  0.09 | loss  0.00 | ppl     1.00
| epoch   0 | 10000/59674 batches | lr 0.002 | ms/batch  3.52 | loss  6.52 | ppl   681.48
| epoch   0 | 20000/59674 batches | lr 0.002 | ms/batch  3.55 | loss  6.26 | ppl   521.80
| epoch   0 | 30000/59674 batches | lr 0.002 | ms/batch  3.53 | loss  6.14 | ppl   465.80
| epoch   0 | 40000/59674 batches | lr 0.002 | ms/batch  3.55 | loss  6.17 | ppl   476.28
| epoch   0 | 50000/59674 batches | lr 0.002 | ms/batch  3.54 | loss  6.19 | ppl   488.79

--- Evaluation ---
-----------------------------------------------------------------------------------------
| end of epoch   0 | valid loss  6.56 | valid ppl   703.05
-----------------------------------------------------------------------------------------

--- Training: 2 ---

.....

--- Training: 20 ---
```

### 1.5 Perplexity on the Test Set for FNN Model without Shared Weights
```
-----------------------------------------------------------------------------------------
| test loss  6.29 | test ppl   539.79
-----------------------------------------------------------------------------------------

1.6 Model Training for FNN Model with Shared Weights.
--- Training: 1 ---
| epoch   0 |     0/59674 batches | lr 0.002 | ms/batch  0.00 | loss  0.00 | ppl     1.00
| epoch   0 | 10000/59674 batches | lr 0.002 | ms/batch  3.52 | loss  6.53 | ppl   682.00
| epoch   0 | 20000/59674 batches | lr 0.002 | ms/batch  3.53 | loss  6.24 | ppl   511.00
| epoch   0 | 30000/59674 batches | lr 0.002 | ms/batch  3.53 | loss  6.09 | ppl   439.74
| epoch   0 | 40000/59674 batches | lr 0.002 | ms/batch  3.53 | loss  6.09 | ppl   440.42
| epoch   0 | 50000/59674 batches | lr 0.002 | ms/batch  3.52 | loss  6.15 | ppl   470.13

--- Evaluation ---
-----------------------------------------------------------------------------------------
| end of epoch   0 | valid loss  6.57 | valid ppl   712.19
-----------------------------------------------------------------------------------------

--- Training: 2 ---

.....

--- Training: 20 ---
```

### 1.6.1 Perplexity on the Test Set for FNN Model without Shared Weights
```
-----------------------------------------------------------------------------------------
| test loss  6.30 | test ppl   544.12
-----------------------------------------------------------------------------------------
```

### 1.7 Text Generation using our FNN Model
1. Alkan became estimated similar Carolina @,@ ft appears in Europe 〈 spectra common starling . Common starlings in Europe
2. Triandos had since two decades such types contemporary Other children = <eos> Midge Doofenshmirtz himself as a lot <unk> and
3. it why species against keeping up is conflict effort to the <unk> style and grades that does not . <eos>
4. Alkan 's motion to keep revival . = <eos> Midge is box scattered 's or [ ] using <unk> <unk>

## Folder Question 2 NER contains code for Question 2 in the Assignment:
1. Run Part4&5.ipnyb to replace lstm layer with CNN and test the model using 1 CNN layer.
2. Run Part6.ipynb to increase the number of convolution layers to change the architecture

----

## Authors

* [Tharakan Rohan Roy](https://github.com/Blitzborg)
* [Gupta Jay](https://github.com/guptajay)
* [Jose Jeswin](https://github.com/Jeswin17)
* [Adrakatti Vivek](https://github.com/VivekAdra31)
* [Dandapath Soham](https://github.com/12dash)


