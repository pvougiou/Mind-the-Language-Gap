# Mind the (Language) Gap
This repository contains the code along with the datasets and the results of the work that has been accepted for the Research track of ESWC 2018. The work focuses on how an adaptation of the encoder-decoder framework can be used to generate articles for underserved language Wikipedias using the [ArticlePlaceholders](https://www.mediawiki.org/wiki/Extension:ArticlePlaceholder).

For a detailed description of the work presented in this repository, please refer to the preprint version of the accepted paper at: <https://2018.eswc-conferences.org/paper_131/>.

## Baselines
The baselines that were used are located in the `baselines` folder. Their respective results along with the results from our model are in the `results` folder.
We work with two baselines of different nature: Machine Translation and Template Retrieval.
The Machine Translation baseline uses the Node.js library https://www.npmjs.com/package/google-translate-api, which helps working around some of the limitations of Google Translate for third-party users. 
Both baselines are easily reproducible, all needed code is contained in the respective folders.

## Community study
The code contained in the `crowdevaluation` folder was made in order to prepare and evaluate the community evaluation. The languages are abbreviated with their respective language codes (ar for Arabic and eo for Esperanto).

- `Preparation` contains files that were used to create the surveys.
  - `Arabic` and `Esperanto` respectively contain:
    - `<languagecode>-final-file`: sample of generated summaries evaluated 
    - `<languagecode>-news-sentences.csv`: sentences of the news corpus
    - `<languagecode>-wikipedia-sentences.csv`: sentences from the original Wikipedia 
  - The `code` folder contains scripts to prepare the corpus according to the requirements of the survey. It contains a README how to use those scripts.
- `Results` contains the result files of the survey, after annonymization and cleaning 
- `evaluation-results` contains scripts that were used to process the results
  - `Arabic` and `Esperanto` respectively contain:
    - `Fluency` for processing the results of the Fluency and Appropriateness survey
      - `<languagecode>-quality.py` calculates scores for the quality in terms of fluency
      - `<languagecode>-approp.py` calculates scores for the quality in terms of fluency
    - `Editors` for processing the results of the Editors 

In the `Models` folder you will find all the necessary files to sample (i.e. beam-sample) from our trained models in both Arabic and Esperanto.

1. First you need to run the shell script located at: `Models/download_trained_models.sh` in order to download all the required trained models and post-processing files.
2. After you follow the instructions and install [Torch](http://torch.ch/) along with the [torch-hdf5](https://github.com/deepmind/torch-hdf5) package on your machine, run `Models/beam-sample.lua`.
3. Make sure that the following Python packages are installed: (i) `h5py`, (ii) `pandas`, and (iii) `numpy` are installed.
3. Run `Models/beam-sample.py` in order to create a `.csv` file with the sampled summaries.

Please bare in mind that you need to have access to a GPU with at least 8 GB of memory in order to sample from the trained models. The experiments were conducted on a single Titan X (Pascal) GPU. For all the possible sampling alterations, please check the comment sections of the above mentioned files.

## Training Details

For the decoder, we used a single layer of GRUs. We set the dimensionality of the decoder's hidden state to 750 in Esperanto and 850 in Arabic case, resulting in 3.375M and 4.335M recurrent connections respectively. We used Batch Normalisation before each non-linear activation function and after each fully-connected layer both on the encoder and the decoder side ([Ioffe and Szegedy 2015](http://proceedings.mlr.press/v37/ioffe15.pdf)), and we initialise all parameters with random uniform distribution between -0.001 and 0.001$.
The networks were trained with mini-batch RMSProp with a learning rate of $0.002$. Each update is computed using a mini-batch of 85 dataset instances. An `l_2` regularisation term over the parameters is also included in the cost function. 
The networks converge after the 8th epoch in the Esperanto case and after the $16$th in the Arabic case. 

We trained all of our models on a single Titan X (Pascal) GPU. In this setup, training in Esperanto and Arabic takes around 30 minutes and 360 minutes respectively. After the 2nd epoch, the learning rate was decayed by 0.8 every epoch. During evaluation and testing, for each unknown set of triples, we do a beam search with a beam size B of 4, and we retain only the summary with the highest probability.
