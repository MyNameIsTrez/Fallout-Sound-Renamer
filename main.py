import os, csv


inputStartFolder = ""
outputStartFolder = ""

filename = "temp.tsv"
# filename = "data.tsv"


tsvFile = open(filename)
tsvRead = csv.reader(tsvFile, delimiter="\t")

next(tsvRead) # Skips the first line containing the header labels.


for row in tsvRead:
    rawVoiceFilePath = row[12]

    inputFilePath = inputStartFolder + rawVoiceFilePath.replace("\\", os.path.sep).replace("sound/voice/fallout4.esm/", "")
    
    fullFileName = os.path.basename(inputFilePath)
    
    fileName = os.path.splitext(fullFileName)[0]

    topicType = row[3]
    outputName = fileName + " | " + topicType

    response = row[10]
    if response != " ":
        outputName += " | " + response

    inputDirPath = os.path.dirname(inputFilePath)
    
    outputFilePath = inputDirPath + outputName

    print("OLD PATH:", inputFilePath)
    print("NEW PATH:", outputFilePath)
    print("---------")

    # os.rename(inputFilePath, outputFilePath)