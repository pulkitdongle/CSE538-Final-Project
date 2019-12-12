import sys
import json

# Reads finalized courses from data.json file and preprocess. Sorts the positive and negative comment,
# and creates separate file for each course for the purpose of training the NLTK's sentiment analysis task to score the summaries.
with open("data.json", "rb") as file:    
    for count, line in enumerate(file):        
        courseJson = json.loads(line[:-2])
        courseName = courseJson["courseName"].replace("/", "_")
        courseName = courseName.replace("?", " ")
        courseName = courseName.replace(" ", "_")
        pos_file = open("train/train_positive_"+courseName+".txt", "a+", encoding='utf-8')        
        pos_file.write(courseJson["positive"])
        pos_file.close()
        neg_file = open("train/train_negative_"+courseName+".txt", "a+", encoding='utf-8')
        neg_file.write(courseJson["negative"])
        neg_file.close()
    file.close()