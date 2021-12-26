import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file_to_separate', type=str, help="this is the file to sepearate into income and expenses")
args = parser.parse_args()
print(args)
print("separating...\n")
