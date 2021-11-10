Q1. Folder Question 1 FNN contains code for Question 1 in the Assignment:
Only PyTorch-FNN.ipynb must be run to load and preprocess the data as well as train the FNN models and observe the output of the models and the generated text. The results including generated text, plots for model loss and model perplexity are present in Question 1 FNN/results.

1.4 Model Training for FNN Model without Shared Weights.
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

1.5 Perplexity on the Test Set for FNN Model without Shared Weights
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

1.6.1 Perplexity on the Test Set for FNN Model without Shared Weights
-----------------------------------------------------------------------------------------
| test loss  6.30 | test ppl   544.12
-----------------------------------------------------------------------------------------

1.7 Text Generation using our FNN Model
1. Alkan became estimated similar Carolina @,@ ft appears in Europe 〈 spectra common starling . Common starlings in Europe
2. Triandos had since two decades such types contemporary Other children = <eos> Midge Doofenshmirtz himself as a lot <unk> and
3. it why species against keeping up is conflict effort to the <unk> style and grades that does not . <eos>
4. Alkan 's motion to keep revival . = <eos> Midge is box scattered 's or [ ] using <unk> <unk>

Q2. Folder Question 2 NER contains code for Question 2 in the Assignment:
Run Part4&5.ipnyb to replace lstm layer with CNN and test the model using 1 CNN layer.
Run Part6.ipynb to increase the number of convolution layers to change the architecture
