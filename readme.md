# Text Summarization

### Introduction: 
A module for summarizing text which uses clustering of skip-thoughts sentence embeddings. Motivation behind this is that, while deciding courses for each semester every SBU student has to go through tons of comments and reviews on Classie Evals (A Stony Brook University portal to view comments of students and stats of the course when it was offered earlier). Reading lengthy comments for multiple courses is quite time consuming. In that case a positive and negative summary about each course would give a rough overall idea about the course while saving time.

### Process: 
 * Web Scraping: The website classie eval is scraped to get all the details about all the courses.
 * Data Preprocessing and Cleaning: Here we strip the data and take only positive and negative reviews along with the                                     course number and ID. Then we parse these fields as JSON objects. To get better                                     results, we discard those courses whose reviews are smaller than 50 words.
 * Sentence Tokenizer: Once we have all the reviews and comments about each course, each comment is split into                        sentences using NLTK’s sentence tokenizer.
 * Skip-Thought Encoder: Used in a supervised manner using Wikipedia data to train it. The model has 2 parts:
   *  Encoder
   *  Decoder
 * Clustering: Sentence embeddings are clustered in high dimensional vector space, with fixed no of clusters. Number 	       of clusters are desired no of sentences in summary.
 * Summarization: Each cluster represents a set of semantically similar sentences. Candidate chosen to be a sentence 		  whose vector representation is closest to the cluster center.

### Setup Instructions:
 * The code is written in Python 2
 * The module uses code of the [Skip-Thoughts paper](http://arxiv.org/abs/1506.06726) which can be found [here](https://github.com/ryankiros/skip-thoughts).
 * The code for the skip-thoughts paper uses [Theano](http://deeplearning.net/software/theano/install.html). Make sure you have Theano installed and GPU acceleration is functional for faster execution.
 * Clone this repository.
 ```
 git clone https://github.com/pulkitdongle/CSE538-Final-Project.git
 ```
 * Install dependecies.
 ``` 
 pip install -r requirements.txt
 python -c 'import nltk; nltk.download("punkt")'
 ```
 * Download the pre-trained models. The total download size will be around 5GB.
 ```
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/utable.npy
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/btable.npy
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
  wget -P ./skip-thoughts/models http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
```
* Verify the MD5 hashes of the downloaded files to ensure that the files were properly downloaded.
```
md5sum skip-thoughts/models/*
```
The output should look like:
```
  9a15429d694a0e035f9ee1efcb1406f3 bi_skip.npz
  c9b86840e1dedb05837735d8bf94cee2 bi_skip.npz.pkl
  022b5b15f53a84c785e3153a2c383df6 btable.npy
  26d8a3e6458500013723b380a4b4b55e dictionary.txt
  8eb7c6948001740c3111d71a2fa446c1 uni_skip.npz
  e1a0ead377877ff3ea5388bb11cfe8d7 uni_skip.npz.pkl
  5871cc62fc01b79788c79c219b175617 utable.npy
```
## How to run?
* Pick a course from classie-evals website and merge all the comments from one of the sections ("What was valuable about this course? or "What could be improved about this course?"). Create a single text file in `/data` as shown by dummy files in `/data`.
* Change the code in main function of `summarize.py` to provide path of the file that you just created above.
```
generate_summary("data/your_file_name.txt")
```
* The summaries will be generated and stored in `/summaries/you_file_name_summ.txt`

### Evaluation:
 * For evaluating summaries, check `/scoreSum`.
   






