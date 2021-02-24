import os
import pandas as pd
from pathlib import Path


filename = "temp.tsv"


i = 0
for chunk in pd.read_table(filename, chunksize=1): # chunksize=1 means reading one line at a time to save on memory.
    voiceFile = chunk["Voice File"][i]

    if pd.notnull(voiceFile): # Don't parse rows without a Voice File value.
        oldFilePath = Path(voiceFile.replace("\\", os.path.sep))
        topicType = chunk["Topic Type"][i]
        response = chunk["Response"][i]

        fileName = oldFilePath.stem

        newName = fileName + " | " + topicType

        if response != " ":
            newName += " | " + response

        # print(repr(newName))

        oldDirPath = oldFilePath.parent
        newFilePath = oldDirPath / newName
        print("OLD PATH:", oldFilePath)
        print("NEW PATH:", newFilePath)
        print("---------")
        # os.rename(oldFilePath, newFilePath)
    
    i += 1 # TODO: Find a cleaner way to track which row is being read.