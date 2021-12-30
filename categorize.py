import pandas as pd
import argparse
from datetime import datetime
import os
import sys


today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="this is the file to categorize")
#parser.add_argument('filters', type=str, help="this is the file that contains your filters")
#parser.add_argument('categories', type=str, help="this is the file that contains your categories")
args = parser.parse_args()

commands = ["exit", "undo", "new_filter"]

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

filters = {}

header5 = ["date", "amount", "idk", "empty1", "details"]
header6 = header5 + ["category"]

def write(df, start):
    current_row_index = start
    print(f"current row: {current_row_index}")
    print(df.loc[[current_row_index]])
    print("enter: value OR a command: " + ', '.join(commands))
    user_input = input()
    if user_input == 'exit':
        sys.exit()
    elif type(user_input) != int or user_input not in commands:
        print('input isnt and interger or in the list of commands')
        write(df, current_row_index)

if not os.path.isdir('.backups'):
    try:
        os.mkdir('.backups')
    except:
        print('error making .backups directory')
if not os.path.isfile(args.file):
    print(f"\n{args.file}" + " cannot be found\n".upper())
    parser.print_help()
elif os.path.isfile(args.file):
    df = pd.read_csv(args.file)
    df_len = len(df.columns)
    if df_len == 5:
        df = pd.read_csv(args.file, names=header5)
        df[header6[5]] = ""
    elif df_len == 6:
        df = pd.read_csv(args.file, names=header6)
    #print(df)

    # number of rows
    print(df.shape[0])
    # first blank link of category column
    start = df["category"].ne('').idxmax()
    write(df, start)

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