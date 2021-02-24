import os, csv


inputStartFolder = ""
outputStartFolder = ""

filename = "temp.tsv"


tsvFile = open(filename)
tsvRead = csv.reader(tsvFile, delimiter="\t")

next(tsvRead) # Skips the first line containing the header labels.


for row in tsvRead:
    rawVoiceFilePath = row[12]

    inputFilePath = inputStartFolder + rawVoiceFilePath.replace("\\", os.sep).replace("sound" + os.sep + "voice" + os.sep + "fallout4.esm" + os.sep, "")

    if (inputFilePath == ""):
        continue # Skips this line.
    
    fullFileName = os.path.basename(inputFilePath)
    
    fileName = os.path.splitext(fullFileName)[0]

    topicType = row[3]
    outputName = fileName + " | " + topicType

    response = row[10]
    if response != " ":
        outputName += " | " + response

    inputDirPath = os.path.dirname(inputFilePath)

    extension = os.path.splitext(fullFileName)[1]
    
    outputFilePath = inputDirPath + outputName + extension

    print("OLD PATH:", inputFilePath)
    print("NEW PATH:", outputFilePath)
    print("---------")

    # os.rename(inputFilePath, outputFilePath)