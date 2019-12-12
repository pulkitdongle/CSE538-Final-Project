from text_summarization import summarize
import sys

def read_text(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    return filedata        

def generate_summary(file_name):
    data = read_text(file_name)
    summary = summarize(data)
    if file_name[7:].startswith('positive'):        
        with open("summaries\\"+file_name[5:-4]+"_summ.txt", "w") as file:
            file.write(". ".join(summary))
    else:
        with open("summaries\\"+file_name[5:-4]+"_summ.txt", "w") as file:
            file.write(". ".join(summary))

def main():
    #generate_summary("cse628_positive.txt")
    generate_summary("data\\cse538_negative.txt")

if __name__ == "__main__":
    main()