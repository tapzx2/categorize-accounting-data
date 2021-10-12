#!/usr/bin/python3

import sys
import os
import csv
import json

commands = ["exit()", "new_common()", "new_category", "back()"]

#files 
common = "common.json"
categories = "categories.json"

def show_help():
    print("""
    NAME
        run.py -- utility to make small business accounting easier
    
    SYNOPSIS
        run.py --separate="FILE_PATH" | --categorize="FILE_PATH" [--common="FILE_PATH"] [--categories="FILE_PATH"]

    DESCRIPTION
        The following options are available:

        --separate    Separate transactions file into income.csv and expenses.csv. Will error if there are transactions of zero.

        --categorize  Adds column to file and prompts user for categorization of each transaction. Once in this mode adjustments to common values and acceptable categorize can be made.
    """)


def confirm_overwrite(input_path):
    if os.path.isfile(input_path):
        user_input = input(f"\n{input_path} will be overwritten\n(y) to continue or quit (any other key)")
        if user_input == 'y':
            return True
        else:
            sys.exit("\nQuitting Program")
    else:
        return True

def line_to_list(line):
    """input: a line from a read csv file
    format file to be readable / editable in python
    output: a list"""
    line = line.replace('\"','')
    line = line.strip()
    split_line = line.split(',')
    return split_line

def append_to(list_to_append, filename = "output.csv"):
    """append list to csv file"""
    with open(filename, 'a') as output_file:
        wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        wr.writerow(list_to_append)

def separate(to_separate):
    """
    separates negative and positive transactions from a wells fargo csv file
    outputs: income.csv, expense.csv
    """
    print(f"...separating {to_separate}")
    fp = open(to_separate, 'r')
    for line in fp:
        line = line_to_list(line)
        number = float(line[1])
        if number < 0:
            append_to(line, "expense.csv")
        elif number > 0:
            append_to(line, "income.csv")
        else:
            print('ERROR: missing edge case, not greather than or less than zero')
            fp.close()
            sys.exit("\nQuitting Program")
    fp.close()
    print('done!')

def create_if_none(file_name):
    if os.path.isfile(file_name) is False:
        file = open(f"{file_name}", "w") 
        file.close()

def load_json(file_name):
    open_file = open(f"{file_name}", 'r')
    return_value = json.load(open_file)
    open_file.close()
    return return_value

def confirm_append(input_path):
    if os.path.isfile(input_path):
        print(f"os path is file {input_path}")
        user_input = input(f"\n{input_path} exists. (continue) where you where left off, (overwrite), or quit (any other key)")
        if user_input == 'continue':
            print('continuing...')
            return True
        elif user_input == 'overwrite':
            print('overwriting...')
            file = open(f"{input_path}", "w") 
            file.close()
            return True
        else:
            sys.exit("\nQuitting Program")
    else:
        return True

def is_common(common, input="string to check"):
    for i in common:
        if i in input:
            return(common[i])
    return(False)


def get_category(print_line, accpt_values_list):
    print("")
    for i in accpt_values_list:
        #print(i, )
        print(i + ' ' * (6 - len(i))  + accpt_values_list[i])
    print("")
    print(print_line)
    print("type number and press enter\n")
    user_value = input()
    try:
        return accpt_values_list[user_value]
    except:
        print("\nERROR: PLEASE TYPE NUMBER FROM LIST")
        return get_category(print_line, accpt_values_list)
 

def categorize(file, output_file_name, common="common.json", categories="categories.json"):
    """
    if confirm_append(output_file):
        file = open(to_categorize)
    else:
        create_if_none(output_file)
        file = open(to_categorize)
    """
    for line in file:
        split_line = line_to_list(line)
        common_value = is_common(common, split_line[4])
        if common_value:
            split_line.append(common_value)
            #print(split_line)
            append_to(split_line, output_file_name)
        else:
            print(split_line)
            value_to_append = get_category(split_line, categories)
            split_line.append(value_to_append)
            append_to(split_line, output_file_name)
            
if sys.argv[1] == "-h":
    show_help()
elif sys.argv[1][:10] == "--separate":
    to_separate = sys.argv[1][11:]
    if os.path.isfile(to_separate):
        if confirm_overwrite("income.csv") and confirm_overwrite("expense.csv"):
            separate(to_separate)
    else:
        sys.exit(f"\ncannot separate \'{to_separate}\', invalid file path")
elif sys.argv[1][:12] == "--categorize":
    to_categorize = sys.argv[1][13:]
    if os.path.isfile(to_categorize):
        create_if_none(common) 
        create_if_none(categories)
        print(common)
        common_values = load_json(common)
        categories_values = load_json(categories)
        output_file_name = to_categorize[:-4] + '_labled.csv'
        print("")
        file = open(to_categorize, 'r')
        categorize(file, output_file_name, common_values, categories_values)
else:
    print("""
    invalid option
    -h for help
    """)

