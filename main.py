import os, csv
from pathlib import Path


inputStartFolder = ""
outputStartFolder = ""

filename = "temp.tsv"
# filename = "data.tsv"


tsvFile = open(filename)
tsvRead = csv.reader(tsvFile, delimiter="\t")

next(tsvRead) # Skips the first line containing the header labels.


for row in tsvRead:
    rawVoiceFilePath = row[12]
    inputFilePath = inputStartFolder / Path(rawVoiceFilePath.replace("\\", os.path.sep).replace("sound/voice/fallout4.esm/", ""))

    fileName = inputFilePath.stem

    topicType = row[3]
    outputName = fileName + " | " + topicType

    response = row[10]
    if response != " ":
        outputName += " | " + response

    inputDirPath = inputFilePath.parent
    outputFilePath = inputDirPath / outputName

    print("OLD PATH:", inputFilePath)
    print("NEW PATH:", outputFilePath)
    print("---------")

    # os.rename(inputFilePath, outputFilePath)