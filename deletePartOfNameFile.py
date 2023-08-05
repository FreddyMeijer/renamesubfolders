import os
import sys
import tkinter as tk
from tkinter import filedialog


def selectFolder():
    folder = filedialog.askdirectory(
        title="Selecteer een map waarin de bestanden hernoemd moeten worden"
    )
    if folder:
        return folder


def removeSubstringFromFilenames(folderPath, substring, logFile):
    with open(logFile, "w") as log:
        files = [name for name in os.listdir(
            folderPath) if os.path.isfile(os.path.join(folderPath, name))]
        for filename in files:
            if substring in filename  and not filename.endswith('.log'):
                newFilename = filename.replace(substring, "")
                oldPath = os.path.join(folderPath, filename)
                newPath = os.path.join(folderPath, newFilename)
                os.rename(oldPath, newPath)
                log.write(f"'{filename}' hernoemd naar '{newFilename}'\n")

if __name__ == "__main__":
    folderPath = selectFolder()
    string = input("Welke woord moet uit de bestandsnaam verwijderd worden? ")
    logFile = folderPath + "\logfile_delete_file_woord.log"
    removeSubstringFromFilenames(folderPath, string, logFile)
    
