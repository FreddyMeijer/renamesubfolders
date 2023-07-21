import os
import sys

def addPrefix(folderPath, prefix, logFile):
    with open(logFile, "w") as log:
        subfolders = [name for name in os.listdir(
            folderPath) if os.path.isdir(os.path.join(folderPath, name))]
        for subfolder in subfolders:
            oldPath = os.path.join(folderPath, subfolder)
            newSubfolder = prefix + subfolder
            newPath = os.path.join(folderPath, newSubfolder)
            os.rename(oldPath, newPath)
            log.write(f"'{subfolder}' renamed to '{newSubfolder}'\n")

if __name__ == "__main__":
    folderPath = r"D:\Naaipatronen-categorie\Sofilantjes"
    prefix = "Sofilantjes - "
    logFile = folderPath + "\logfile_add_prefix.log"
    addPrefix(folderPath, prefix, logFile)
