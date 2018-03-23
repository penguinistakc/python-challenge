#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
PyBank -- analyze financial records consisting of date and revenue.
Provide total amount of months in dataset, amount of revene gained over
entire period, average change in revenue over period, greatest increase
in revenue over period, greatest decrease in revenue over the period.
"""
import os
import csv
import pathlib

#file information
# name of input file
input_file = "budget_test.csv"

#directory where input file is located
input_dir = "raw_data"

#name of output file
output_file = "budget_test.output.txt"

#directory where output file should be located (should be a subdirectory of present working directory)
output_dir = "output"

# initialize variables
first_month = True
total_number_months_in_dataset = 0
total_revenue_over_period = 0.0
revenue_change_tracker = []
last_month_revenue = 0
amount_greatest_increase_in_revenue = 0.0
month_greatest_increase_in_revenue = ""
month_greatest_decrease_in_revenue = ""
amount_greatest_decrease_in_revenue = 0.0   

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
    


    

def calculate_change_in_revenue(new_revenue, old_revenue):
    """
    calculate monthly change in revenue
    """
    return new_revenue - old_revenue

def calculate_total_revenue(new_revenue, running_total):
    """
    calculate total revenue over the file
    """
    return new_revenue + running_total

def create_financial_analysis(total_number_months_in_dataset, total_revenue_over_period, 
                              revenue_change_tracker, month_greatest_increase_in_revenue,
                              amount_greatest_increase_in_revenue, amount_greatest_decrease_in_revenue, 
                              month_greatest_decrease_in_revenue):

    header_line = ('-' * 30)

    financial_analysis = (
f' Financial Analysis\n \
{header_line}\n \
Total Months: {total_number_months_in_dataset}\n \
Total Revenue: ${total_revenue_over_period}\n \
Average Revenue Change: ${sum(revenue_change_tracker) / len(revenue_change_tracker)}\n \
Greatest Increase in Revenue: {month_greatest_increase_in_revenue} (${amount_greatest_increase_in_revenue})\n \
Greatest Decrease in Revenue: {month_greatest_decrease_in_revenue} (${amount_greatest_decrease_in_revenue})\n ')

    #print to standard output
    print(financial_analysis)

    #print to file
    #with open("output.txt", "w") as outputfile:
    #    outputfile.write(financial_analysis)
    with open_file(output_dir, output_file, "w") as outputfile:
        outputfile.write(financial_analysis)


if __name__ == '__main__':

    #open file
    with open_file(input_dir, input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        #ignore first (header) row
        next(reader)
        # treat each line as a separate row
        for row in reader:
            period = row[0]
            monthly_revenue = float(row[1])
            # Change in revenue should begin calculating in the second period, based on changes from period 1 to period 2. Therefore, first month's revenue
            # is excluded from the change_in_revenue calculation.
            if first_month == True:
                last_month_revenue = monthly_revenue
                change_in_revenue = 0.0
                first_month = False
            else:
                change_in_revenue = calculate_change_in_revenue(monthly_revenue, last_month_revenue)
                revenue_change_tracker.append(change_in_revenue)
                last_month_revenue = monthly_revenue
        
            # simple counter to tally rows
            total_number_months_in_dataset += 1
            total_revenue_over_period = calculate_total_revenue(total_revenue_over_period,  monthly_revenue)

        if change_in_revenue > amount_greatest_increase_in_revenue:
            amount_greatest_increase_in_revenue = change_in_revenue
            month_greatest_increase_in_revenue = period

        if change_in_revenue < amount_greatest_decrease_in_revenue:
            amount_greatest_decrease_in_revenue = change_in_revenue
            period_greatest_decrease_in_revenue = period

    create_financial_analysis(total_number_months_in_dataset, total_revenue_over_period, revenue_change_tracker, month_greatest_increase_in_revenue,
                               amount_greatest_increase_in_revenue, amount_greatest_decrease_in_revenue, month_greatest_decrease_in_revenue)