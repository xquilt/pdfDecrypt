from os.path import isfile
import argparse

parser = argparse.ArgumentParser(
    description='Crack protected pdf files using plain brute force!',
    allow_abbrev=True
)

parser.add_argument('-v', '--version', help='Show project version number')
parser.add_argument('-c', '--check', help='Check the protection on a pdf file(s)')
parser.add_argument('-s', '--start', help='The start number for brute force')
parser.add_argument('-e', '--end', help='The end number for brute force')
parser.add_argument('-p', '--path', help='The path to the pdf file')
parser.add_argument('-f' '--verbose', help='Show [f]ailed password trial attempts. Default is being suppressed!')

argumentsObject = parser.parse_args()

# Check if the passed filepath is valid
