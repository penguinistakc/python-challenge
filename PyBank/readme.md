# PyBank

PyBank -- analyze financial records consisting of date and revenue.
Provide total amount of months in dataset, amount of revenue gained over
entire period, average change in revenue over period, greatest increase
in revenue over period, greatest decrease in revenue over the period. Presents
a report on standard output and a text file.

## Usage

The script does not yet accept command line arguments. User needs to tell the script where the input and output files are
using the following variables in the script:
* *input_file:* string; file name of the input file to be processed
* *input_dir:* string; name of directory in which input file resides (usually a subdirectory of directory where script resides)
* *output_file:* string; file name of the output file -- script will create this directory if it does not exist, will use it if it does.
* *output_dir:* string; name of directory in which output file resides (usually a subdirectory of directory where script resides)
