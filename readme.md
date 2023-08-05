## Renaming folders
These two Python scripts rename subfolders in a folder. There are two files. One to add a prefix to a subfolder (*addPrefix.py*) and one to delete a prefix or a part of the subfoldername (*deletePrefix.py*).

## Installation
To install the renamesubfolders all you need to do is:

- Download and install an instance of Python
- Open your terminal navigate to the desired folder and use `git clone https://github.com/FreddyMeijer/renamesubfolders.git`
- Open the folder in which the git was cloned
- Run the desired function by using e.g. `python3 addPrefix.py`

## addPrefix (folder only)
The user will be asked to select a rootfolder in which the folders will be renamed. After selection the user is asked to define a prefix (in terminal). After executing there will be a logfile created in the rootfolder with the name *logfile_add_prefix.log*

## deletePartOfName (folder and file)
The user will be asked to select a rootfolder in which the folders or files will be renamed. After selection the user is asked to define a string (in terminal). The deletion of a part of the name will be done when the string is found in the name. So for example:

I have a subfolder with the following name *Freddy_personal_finance* and I run the script. The string I entered is *_personal_*, so the new name will be *Freddyfinance*

In the rootfolder there will be a logfile created with the name *logfile_delete_woord.log*