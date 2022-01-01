import pandas as pd
import argparse
from datetime import datetime
import os
import sys
import json

today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="this is the file to categorize")
#parser.add_argument('filters', type=str, help="this is the file that contains your filters")
#parser.add_argument('categories', type=str, help="this is the file that contains your categories")
args = parser.parse_args()

def exit_program():
    print('exiting program...')
    sys.exit()

def new_filter():
    print("creating filter...")
    #print(df.at[start_index, 'category'])
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

#filters = {
#    "Aoufe":"Rent",
#    "SRP SUREPAY": "Utilities",
#    "Cleaner": "Janitor and cleaning"}

filter_file = "filters.json"

def load_json(file_name):
    open_file = open(f"{file_name}", 'r')
    return_value = json.load(open_file)
    open_file.close()
    return return_value

filters = load_json(filter_file)

header5 = ["date", "amount", "idk", "empty1", "details"]
header6 = header5 + ["category"]

def filter(df, filters):
    print("running filter program...")
    for key, value in filters.items():
        df.loc[df['details'].str.contains(key, case=False), "category"] = value
    return df

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
        df = pd.read_csv(args.file)
        df_len = len(df.columns)
        if df_len == 5:
            df = pd.read_csv(args.file, names=header5)
            df[header6[5]] = "uncategorized"
            return df
        elif df_len == 6:
            df = pd.read_csv(args.file, names=header6)
            return df
    #os.rename(f"./{args.file}", f"./.backups/{args.file}_{today}")

df = prepare()

if 'uncategorized' in df['category'].values:
    previously_written_row = -1
    while 'uncategorized' in df['category'].values:
        print("time to categorize!")
        #start_index = df["category"].eq('uncategorized').idxmax()
        #print(df.iloc[start_index:start_index+1])
        # WORKING FROM HERE!!! LOOK LOOK HERE!!!
        filter(df, filters)
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
        
        #print(df)

        # get user input
        # if user_input = command
            # run it
        # elif user_input in range of values for categories
            # update df row value
            # write to temp file in case program crashes
        # else
            # let user know it was an invalid entry and we're trying again!
        
else:
    print('no uncategorized values found')
#
# print(df["category"])
#print(df["category"].eq('uncategorized'))
#print(df["category"].eq('uncategorized').idxmax())
#print(type(df["category"].ne('uncategorized').idxmax()))
#while df["category"].ne('').idxmax() != False:
#    print("while loop running")
        # number of rows
        #print(df.shape[0])
        #df = filter(df, filters)
        #start = df["category"].ne('').idxmax()
        #write(df, start)
        
    

    # first blank link of category column
    
    

    # filter()
    
    # filter()
    # start = starting_position() - done
    # write(start)
        # current_line = start - done
        # if data entry is normal, continue write
        # elif data entry is undo, go back one
        # elif data entry is new_filter
            # create_new_filter()
            # filter ()
            # write(start)
        #elif data entry is exit, quit - done
        # else, invalid entry error
    #read 

    # filter(new_filter())