import os
import sys

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
                log.write(f"'{subfolder}' is hersteld naar '{newSubfolder}'\n")

if __name__ == "__main__":
    folderPath = r"C:\Users\fredd\OneDrive - Servicepunt 71\Playgrounds\Repros\RenameSubfolders"
    prefix = "test - kids - "
    logFile = folderPath + "\logfile.log"
    removePrefix(folderPath, prefix, logFile)
