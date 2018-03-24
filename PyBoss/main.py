#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
PyBoss - convert employee data: split name into first and last name fields, mask social security numbers, 
convert long state name to state abbreviation
"""

import os
import csv
import pathlib
#courtesy of afhaque/us_state_abbrev.py -- no license found
import us_state_abbrev


#file information
# name of input file
input_file = "employee_data2.csv"

#directory where input file is located
input_dir = "raw_data"

#name of output file
output_file = "employee_data2.output.txt"

#directory where output file should be located (should be a subdirectory of present working directory)
output_dir = "output"

#initialize lists for row and file
output_row = []
new_file = []

def open_file(file_dir, file_name, mode):
    """ if mode == "w", check for existence of output directory, and create if necessary
        otherwise, assume this is a read operation
    """
    file_path = os.path.join(file_dir,file_name)
    if mode == "w":
        pathlib.Path(file_dir).mkdir(parents=True, exist_ok=True)
        return open(file_path,"w")
    elif mode == "a":
        pathlib.Path(file_dir).mkdir(parents=True, exist_ok = True)
        return open(file_path,"a")
    else:
        #assume we are reading file
        return open(file_path)

def write_file(file):
    """logic to write out file at completion of loop
    arg: file (object), output_dir (string), output_file (string)
    output_dir and output_file are defined at the top of the script
    """
    with open_file(output_dir, output_file, "w") as outputfile:
        writer = csv.writer(outputfile)
        writer.writerows(file)
        

def format_name(name):
    """split name into first and last names
    arg: name (string)
    """
    first_name, last_name = name.split(' ')
    return first_name, last_name

def format_dob(dob):
    """reformat date of birth
    arg: dob (string) -- date of birth from input file
    """
    year, month, day = dob.split('-')
    return f'{day}/{month}/{year}'

def mask_ssn(ssn):
    """mask first five digits of ssn with asterisks
    arg: ssn (string)
    """
    first_group, second_group, third_group = ssn.split('-')
    first_group = "***"
    second_group = "**"

    return f'{first_group}-{second_group}-{third_group}'

def format_state(state):
    """find long-form state name in state abbreviation dictionary 
    and return abbreviation
    arg: state (string)
    """
    return us_state_abbrev.us_state_abbrev.get(state)

def main():
    """main loop for reading and processing input, writing output"""
    first_row = True
    output_row = []
    #open file for reading
    with open_file(input_dir, input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #initialize row variables
            emp_id = row[0]
            name = row[1]
            dob = row[2]
            ssn = row[3]
            state = row[4]
            #use input header row to populate output header row, add extra fields
            if first_row == True:
                new_file.append([emp_id, "First Name", "Last Name", dob, ssn, state])
                first_row = False
            else:
                #build data rows after input header has been processed
                output_row.append(emp_id)
                first_name, last_name = format_name(name)
                output_row.append(first_name)
                output_row.append(last_name)
                output_row.append(format_dob(dob))
                output_row.append(mask_ssn(ssn))
                output_row.append(format_state(state))
                #append output_row to the new output file list
                new_file.append(output_row)
                #empty out the output row after it has been appended to the output file
                output_row = []

    #write file at conclusion of loop
    write_file(new_file)

if __name__ == "__main__":
    main()