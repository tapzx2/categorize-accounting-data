import pandas as pd
import sys
#print('\n'.join(sys.path))
import os
import argparse
from datetime import datetime

today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="this is the file to sepearate into income and expenses")
args = parser.parse_args()

def move_old():
    files = ["expense.csv", "income.csv", args.file]
    for file in files:
        if os.path.isfile(file):
            os.rename(f"./{file}", f"./.backups/{file}_{today}")

if not os.path.isdir('.backups'):
    try:
        os.mkdir('.backups')
    except:
        print('error making .backups directory')
if not os.path.isfile(args.file):
    print(f"\n{args.file}" + " cannot be found\n".upper())
    parser.print_help()
elif os.path.isfile(args.file):
    print("\nseparating..." + args.file)
    print(f'\n{args.file} and previous versions of income.csv and expense.csv\n have been moved to .backups\n')
    df = pd.read_csv(args.file, names=["date", "amount", "idk", "empty1", "details"])
    income = df[df['amount'] > 0]
    expense = df[df['amount'] < 0]
    move_old()
    income.to_csv('./income.csv', index=False, header=False)
    expense.to_csv('./expense.csv', index=False, header=False)