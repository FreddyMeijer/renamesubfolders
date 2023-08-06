import os
import sys
import tkinter as tk
from tkinter import filedialog


def selectFile():
    file = filedialog.askdirectory(
        title="Selecteer een map waarin de bestanden hernoemd moeten worden"
    )
    if file:
        return file


def addPrefix(filePath, prefix, logFile):
    with open(logFile, "w") as log:
        files = [name for name in os.listdir(
            filePath) if os.path.isfile(os.path.join(filePath, name))]
        for file in files:
            if file != os.path.basename(logFile):
                oldPath = os.path.join(filePath, file)
                newfile = prefix + file
                newPath = os.path.join(filePath, newfile)
                os.rename(oldPath, newPath)
                log.write(f"'{file}' hernoemd naar '{newfile}'\n")


if __name__ == "__main__":
    filePath = selectFile()
    prefix = input("Welke prefix moeten de bestanden krijgen? ")
    logFile = filePath + "\logfile_add_prefix.log"
    addPrefix(filePath, prefix, logFile)
