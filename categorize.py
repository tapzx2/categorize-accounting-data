import pandas as pd
import argparse
from datetime import datetime
import os


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

if not os.path.isdir('.backups'):
    try:
        os.mkdir('.backups')
    except:
        print('error making .backups directory')
if not os.path.isfile(args.file):
    print(f"\n{args.file}" + " cannot be found\n".upper())
    parser.print_help()
elif os.path.isfile(args.file):
    # filter()
    # start = starting_position()
    # write(start)
        # current_line = start
        # if data entry is normal, continue write
        # elif data entry is undo, go back one
        # elif data entry is new_filter
            # create_new_filter()
            # filter ()
            # write(start)
        #elif data entry is exit, quit
        # else, invalid entry error
    #read 

    # filter(new_filter())


