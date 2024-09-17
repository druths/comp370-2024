from argparse import ArgumentParser
import os.path
import json
import csv


def main():
    parser = ArgumentParser()
    parser.add_argument("--ifile", help="input file", required=True)
    args = parser.parse_args()

    transform_fname = os.path.join(os.path.dirname(__file__), "full_names.json")

    print(transform_fname)
    with open(transform_fname, "r") as f:
        full_names = json.load(f)

    print_csv(args.ifile)


def print_csv(fname):
    reader = csv.reader(open(fname, "r"))

    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
