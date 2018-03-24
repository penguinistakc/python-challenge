#!/usr/bin/env python
# # -*- coding: utf-8 -*-
import os
import csv
import pathlib
#courtest of afhaque/us_state_abbrev.py -- no license found
import us_state_abbrev


#file information
# name of input file
input_file = "employee_test_3.csv"

#directory where input file is located
input_dir = "raw_data"

#name of output file
output_file = "employee_test.output.txt"

#directory where output file should be located (should be a subdirectory of present working directory)
output_dir = "output"

# input column variables
emp_id = ""
name = ""
dob = ""
ssn = ""
state = ""


#output column variables
employee_id = ""
first_name = ""
last_name = ""
date_of_birth = ""
state_abbrev = ""

#list for output row
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
    else:
        #assume we are reading file
        return open(file_path)

def write_file(file):
    with open_file(output_dir, output_file, "w") as outputfile:
        writer = csv.writer(outputfile)
        writer.writerows(file)
        

def format_name(name):
    first_name, last_name = name.split(' ')
    return first_name, last_name

def format_dob(dob):
    year, month, day = dob.split('-')
    return f'{day}/{month}/{year}'

def format_ssn(ssn):
    
    first_group, second_group, third_group = ssn.split('-')
    first_group = "***"
    second_group = "**"

    return f'{first_group}-{second_group}-{third_group}'

def format_state(state):
    return us_state_abbrev.us_state_abbrev.get(state)

def main():
    first_row = True
    #open file for reading
    with open_file(input_dir, input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            emp_id = row[0]
            name = row[1]
            dob = row[2]
            ssn = row[3]
            state = row[4]
            if first_row == True:
                new_file.append([emp_id, "First Name", "Last Name", dob, ssn, state])
                #write_row(output_row)
                output_row = []
                first_row = False
            else:
                output_row.append(emp_id)
                first_name, last_name = format_name(name)
                output_row.append(first_name)
                output_row.append(last_name)
                output_row.append(format_dob(dob))
                output_row.append(format_ssn(ssn))
                output_row.append(format_state(state))
                new_file.append(output_row)
                print(output_row)
                #write_row(output_row)
                output_row = []

    write_file(new_file)

if __name__ == "__main__":
    main()