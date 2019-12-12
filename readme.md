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


### Evaluation:
 * For evaluating summaries, check scoreSum. 
# Acknowledgement

 * Skip-Thoughts encoder-decoder: https://github.com/ryankiros/skip-thoughts

 
   






