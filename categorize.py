import pandas as pd
import argparse
from datetime import datetime
import os
import sys
import json

# used append today to backup files
today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# parse given command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="this is the file to categorize")
args = parser.parse_args()

# helper function
def create_if_none(file_name):
    if os.path.isfile(file_name) is False:
        file = open(f"{file_name}", "w") 
        file.close()

# user commands
def exit_program():
    print('exiting program...')
    sys.exit()

def new_filter():
    print("creating filter...")
    print("input a string to match on from details")
    user_input_match = input()
    print("input the number to map to from data value")
    user_input_map = input()
    try:
        if int(user_input_map) in range (0, len(categories)):
            filters[user_input_match] = categories[int(user_input_map)]
            with open(filter_file, 'w') as outfile:
                json.dump(filters, outfile, indent=4)
    except:
        print("user input: " + user_input_map)
        print("this input is no good, please try again")
        new_filter()

def undo():
    print("undoing previous entry...")
    if previously_written_row == -1:
        print("sorry, can't undo. nothing has been entered yet")
    else:
        df.at[previously_written_row, 'category'] = "uncategorized"

commands = {
    "exit": exit_program,
    "new_filter": new_filter,
    "undo": undo
}

command_keys = [key for key in commands.keys()]

# available categories
# feel free to edit the categories to suit your needs
categories = [
    "Advertising",
    "Insurance",
    "Legal fees and professional services",
    "Meals",
    "Office expenses",
    "Rent",
    "Repairs and maintenance",
    "Supplies",
    "Taxes and licenses",
    "Utilities",
    "Interbusiness account transfer",
    "Owner draw",
    "Janitor and cleaning"
]
categories_str = ''
for i in range(0, len(categories)):
    categories_str += f'{i} : {categories[i]}\n'

# loading and managing filters
filter_file = "filters.json"

def load_json(file_name):
    create_if_none(file_name)
    open_file = open(f"{file_name}", 'r')
    return_value = json.load(open_file)
    open_file.close()
    return return_value

filters = load_json(filter_file)

def filter(df, filters):
    print("running filter program...")
    for key, value in filters.items():
        df.loc[df['details'].str.contains(key, case=False), "category"] = value
    return df

# csv headers
# these can be changed based on the file you're loading
# expect to do some debugging ;)
header5 = ["date", "amount", "idk", "empty1", "details"]
header6 = header5 + ["category"]

# make backups directory and load input file as df
def prepare():
    if not os.path.isdir('.backups'):
        try:
            os.mkdir('.backups')
        except:
            print('error making .backups directory')
    if not os.path.isfile(args.file):
        print(f"\n{args.file}" + " cannot be found\n".upper())
        parser.print_help()
        exit_program()
    elif os.path.isfile(args.file):
        print('path is file')
        df = pd.read_csv(args.file)
        df_len = len(df.columns)
        # file has never been categorized before
        if df_len == 5:
            df = pd.read_csv(args.file, names=header5)
            df[header6[5]] = "uncategorized"
            return df
        # file has been touched by categorize.py before
        elif df_len == 6:
            df = pd.read_csv(args.file, names=header6)
            return df
        else:
            print("    issue here")
    else:
        print('issue preparing, nothing returned')

df = prepare()
print(df)

# main loop
if 'uncategorized' in df['category'].values:
    os.rename(f"./{args.file}", f"./.backups/{args.file}_{today}")
    previously_written_row = -1
    while 'uncategorized' in df['category'].values:
        print("time to categorize!")
        filter(df, filters)
        df.to_csv(args.file, header=None, index=None)
        start_index = df["category"].eq('uncategorized').idxmax()
        print("\n===================\n")
        print(df.iloc[start_index:start_index+1])
        print(f"\nenter a command: {command_keys}\n")
        print(f"or enter a data value:\n{categories_str}")
        user_input = input()
        for key, value in commands.items():
            if user_input == key:
                value()
        try:
            if int(user_input) in range (0, len(categories)):
                print(f"{user_input} selected")
                df.at[start_index, 'category'] = categories[int(user_input)]
                previously_written_row = start_index
                print(f"write() previously written row: {previously_written_row}")
            else:
                print("that number isn't a category")
        except:
            print("nothing written...")

        else:
            print("continuing...")
else:
    print('no uncategorized values found')
