import os
import sys
import tkinter as tk
from tkinter import filedialog


def selectFolder():
    folder = filedialog.askdirectory(
        title="Selecteer een map waarin de submapen hernoemd moeten worden"
    )
    if folder:
        return folder


def removePrefix(folderPath, prefix, logFile):
    with open(logFile, "w") as log:
        subfolders = [name for name in os.listdir(
            folderPath) if os.path.isdir(os.path.join(folderPath, name))]
        for subfolder in subfolders:
            if subfolder.startswith(prefix):
                oldPath = os.path.join(folderPath, subfolder)
                newSubfolder = subfolder[len(prefix):]
                newPath = os.path.join(folderPath, newSubfolder)
                os.rename(oldPath, newPath)
                log.write(f"'{subfolder}' hernoemd naar '{newSubfolder}'\n")

if __name__ == "__main__":
    folderPath = selectFolder()
    prefix = input("Welke prefix moeten van de mapnaam verwijderd worden? ")
    logFile = folderPath + "\logfile_delete_prefix.log"
    removePrefix(folderPath, prefix, logFile)
