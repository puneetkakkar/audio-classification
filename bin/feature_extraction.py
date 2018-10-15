from argparse import ArgumentParser
from pyaudioclassification import feat_extract

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input",
                    help="path to data directory")
parser.add_argument("-m", "--mode", dest="mode",
                    help="add to force either 'binary' or 'categorical' crossentropy")
parser.add_argument("-t", "--t", dest="type", default="CNN",
                    help="type of ML model to train. can be either 'SVM', 'NN', or 'CNN'. defaults to CNN")

args = parser.parse_args()
if (args.input == None):
    raise ValueError("No input directory provided. Use the -i flag to specifiy the directory where your data is stored.")

feature_extraction(args.input)
