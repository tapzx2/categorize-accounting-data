#source: https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3

'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, required=True)

args = parser.parse_args()

print('Hello', args.name)
'''

# accounting data test

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--separate', type=str, required=False)
parser.add_argument('--categorize', type=str, required=False)
args = parser.parse_args()
print(args)
