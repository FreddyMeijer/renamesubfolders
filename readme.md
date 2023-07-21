# ENGLISH
These two Python scripts rename subfolders in a folder. There are two files. One to add a prefix to a subfolder (*addPrefix.py*) and one to delete a prefix or a part of the subfoldername (*deletePrefix.py*).

## addPrefix.py
**Please change the following lines:**
- line 16: Change the path of the rootfolder in which you want to change the subfoldersname. Place the name between quotes (")
- line 17: Specify the prefix. Place the prefix between quotes (")

In the rootfolder there will be a logfile created with the name *logfile_add_prefix.log*

## deletePrefix.py
**Please change the following lines:**
- line 17: Change the path of the rootfolder in which you want to change the subfoldersname. Place the name between quotes (")
- line 18: Specify the prefix. Place the prefix between quotes (")

De deletion of a part of the name (most likely the prefix) will be done from character one of the subfoldername. So for example:

I have a subfolder with the following name *Freddy_personal_finance* and I run the script. I change the prefix on line 18 to *_personal_*. Nothing will happen. The correct prefix would be *Freddy_personal_*. If the script is executed with the correct prefix, the new name will be *finance*

In the rootfolder there will be a logfile created with the name *logfile_delete_prefix.log*

## NEDERLANDS
Deze twee Python scripts hernoemen submappen binnen een map. Dit kan via twee bestanden. Eentje die een prefix voor een mapnaam plaatst (*addPrefix.py*) en een andere die een deel van de naam van een map weghaalt (*deletePrefix.py*).

## addPrefix.py
- regel 16: Verander de padnaam naar de rootmap waarin je de submappen wilt hernoemen. Plaats de naam tussen de quotes (")
- regel 17: Bepaal de prefix. Plaats de prefix tussen de quotes (")

In de rootmap wordt een logbestand aangemaakt met de naam *logfile_add_prefix.log*

## deletePrefix.py
**Verander de volgende regels:**
- regel 17: Verander de padnaam naar de rootmap waarin je de submappen wilt hernoemen. Plaats de naam tussen de quotes (")
- regel 18: Bepaal de prefix. Plaats de prefix tussen de quotes (")

De verwijdering van een deel van de naam (waarschijnlijk een eerder gemaakte prefix) gebeurt vanaf het eerste karakter van de naam. Bijvoorbeeld":

Ik heb een submap met de naam *Freddy_personal_finance*. Ik draai het script waarin ik de prefix heb vastgesteld op *_personal_*. Er zal nu niets gebeuren. De juiste prefix zou namelijk *Freddy_personal_* zijn. Als je die prefix zou gebruiken, wordt de nieuwe mapnaam *finance*.

In de rootmap wordt een logbestand aangemaakt met de naam *logfile_delete_prefix.log*