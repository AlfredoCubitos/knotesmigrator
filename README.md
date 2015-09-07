# Knotes Migrator
## Tool for migrating knotes ics files

This is a small python script that helps to get notes from the knotes ics file.

Or more precisely, this extracts the content into plain text files.
The file name is the subject of the note.

Also its possible to store the whole content into a json file for post processing.

Calling `#> notesmigrator ` extracts all the notes and writes the content into plain text files in the same directory

The script asumes that the ics file  in the useers home directory beneath `.kde4/share/apps/knotes/`
If your kde directory has a different location, change the `path` variable in the script

`#> notesmigrator json` creates a big json file for post processing


