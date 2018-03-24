#PyBoss
PyBoss - convert employee data: split name into first and last name fields, mask social security numbers, 
convert long state name to state abbreviation

##Usage
The script does not yet accept command line arguments. User needs to tell the script where the input and output files are
using the following variables in the script:
input_file: string; file name of the input file to be processed
input_dir: string; name of directory in which input file resides (usually a subdirectory of directory where script resides)
output_file: string; file name of the output file -- script will create this directory if it does not exist, will use it if it does.
output_dir: string; name of directory in which output file resides (usually a subdirectory of directory where script resides)