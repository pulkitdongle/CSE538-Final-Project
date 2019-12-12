import json
newDict = {}

opFile = open("data.json", "a")
# from final.json we extract only positive(valuableComm) and negative(improvedComm) comments and save them to data.json which will be used by dataprocessor.py
# to create a separate file for each course as the training data for the scoring the summaries that we generate from skip-thoughts.
with open("final.json", "r") as fp:
    for count, line in enumerate(fp):            
        lineDict = json.loads(line)

        positive = ' '.join(x for x in lineDict["valuableComm"])
        negative = ' '.join(x for x in lineDict["improvedComm"])        
        
        if(len(positive.split()) >= 500 or len(negative.split()) >= 500):
            newDict['courseCode'] = lineDict["code"]
            newDict['courseName'] = lineDict["courseName"]
            newDict['positive'] = positive
            newDict['negative'] = negative
            
            json.dump(newDict, opFile)
            opFile.write(",\n")

opFile.close()
