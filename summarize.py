import pandas as pd
import sys
#print('\n'.join(sys.path))
import os
import argparse
from datetime import datetime

today = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="this is the file you want to summarize")
args = parser.parse_args()

def move_old():
    files = [f"summarized_{args.file}"]
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
    print("\nsummarizing..." + args.file)
    print(f'previous versions of \nsummarized_{args.file} have been moved to .backups\n')
    df = pd.read_csv(args.file, names=["date", "amount", "idk", "empty1", "details", "category"])
    sums = df.groupby('category', as_index=False).agg({'amount':'sum'}).rename(columns={'amount':'total'})
    print(sums)
    move_old()
    sums.to_csv(f'./summarized_{args.file}', index=False, header=True)
    print(f'\nsummary:\nsummarized_{args.file}\n')