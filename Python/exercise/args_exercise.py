import argparse

"""
python args_exercise.py --train
python args_exercise.py --test
"""

parser = argparse.ArgumentParser(description='demo')
parser.add_argument('--train', dest='train', action='store_true')
parser.add_argument('--test', dest='test', action='store_true')
args = parser.parse_args()
if args.train: 
    print('train')
if args.test:
    print('test')
