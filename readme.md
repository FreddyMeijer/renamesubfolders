## Renaming folders
These two Python scripts rename subfolders in a folder. There are two files. One to add a prefix to a subfolder (*addPrefix.py*) and one to delete a prefix or a part of the subfoldername (*deletePrefix.py*).

## Installation
To install the renamesubfolders all you need to do is:

- Download and install an instance of Python
- Open your terminal navigate to the desired folder and use `git clone https://github.com/FreddyMeijer/renamesubfolders.git`
- Open the folder in which the git was cloned
- Run the desired function by using e.g. `python3 addPrefix.py`

## addPrefix.py
The user will be asked to select a rootfolder in which the folders will be renamed. After selection the user is asked to define a prefix (in terminal). After executing there will be a logfile created in the rootfolder with the name *logfile_add_prefix.log*

## deletePrefix.py
The user will be asked to select a rootfolder in which the folders will be renamed. After selection the user is asked to define a prefix (in terminal). The deletion of a part of the name (most likely the prefix) will be done from character one of the subfoldername. So for example:

I have a subfolder with the following name *Freddy_personal_finance* and I run the script. I change the prefix on line 18 to *_personal_*. Nothing will happen. The correct prefix would be *Freddy_personal_*. If the script is executed with the correct prefix, the new name will be *finance*

In the rootfolder there will be a logfile created with the name *logfile_delete_prefix.log*