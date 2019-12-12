"""
Module for Text Summarization

*****************************************************************************
Input Parameters:
    comments: A list of strings containing the comments

Returns:
    summary: A list of strings containing the summaries.
*****************************************************************************
"""


# ***************************************************************************
import numpy as np
from nltk.tokenize import sent_tokenize
import skipthoughts
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
# ***************************************************************************


def preprocess(comments):
    """
    Performs preprocessing operation:        
        Removing new line characters.
    """
    n_comments = len(comments)
    for i in range(n_comments):
        comment = comments[i]        
        lines = comment.split('\n')
        for j in reversed(range(len(lines))):
            lines[j] = lines[j].strip()
            if lines[j] == '':
                lines.pop(j)
        comments[i] = ' '.join(lines)
        
        
def split_sentences(comments):
    """
    Splits the comments into individual sentences
    """
    n_comments = len(comments)
    for i in range(n_comments):
        comment = comments[i]
        sentences = sent_tokenize(comment)
        for j in reversed(range(len(sentences))):
            sent = sentences[j]
            sentences[j] = sent.strip()
            if sent == '':
                sentences.pop(j)
        comments[i] = sentences
        
        
def skipthought_encode(comments):
    """
    Obtains sentence embeddings for each sentence in the comments
    """
    enc_comments = [None]*len(comments)
    cum_sum_sentences = [0]
    sent_count = 0
    for comment in comments:
        sent_count += len(comment)
        cum_sum_sentences.append(sent_count)

    all_sentences = [sent for comment in comments for sent in comment]
    print('Loading pre-trained models...')
    model = skipthoughts.load_model()
    encoder = skipthoughts.Encoder(model)
    print('Encoding sentences...')
    enc_sentences = encoder.encode(all_sentences, verbose=False)

    for i in range(len(comments)):
        begin = cum_sum_sentences[i]
        end = cum_sum_sentences[i+1]
        enc_comments[i] = enc_sentences[begin:end]
    return enc_comments
        
    
def summarize(comments):
    """
    Performs summarization of comments
    """
    n_comments = len(comments)
    summary = [None]*n_comments
    print('Preprecesing...')
    preprocess(comments)
    print('Splitting into sentences...')
    split_sentences(comments)
    print('Starting to encode...')
    enc_comments = skipthought_encode(comments)
    print('Encoding Finished')
    for i in range(n_comments):
        enc_comment = enc_comments[i]
        n_clusters = int(np.ceil(len(enc_comment)**0.5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans = kmeans.fit(enc_comment)
        avg = []
        closest = []
        for j in range(n_clusters):
            idx = np.where(kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_,\
                                                   enc_comment)
        ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        summary[i] = ' '.join([comments[i][closest[idx]] for idx in ordering])
    print('Clustering Finished')
    return summary
      