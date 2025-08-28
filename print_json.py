import json
import sys
import argparse


def load_json(args):
        # Load data from provided JSON file
        print("Processing json input file: ", args.jsonfile[0])
        try:
                with open(args.jsonfile[0], 'r') as jsonfile:
                        jsondata = json.load(jsonfile)
                        return jsondata
        except FileNotFoundError:
                print(f"Error: the file '{args.jsonfile}' was not found")
        except json.JSONDecodeError:
                print(f"Error: the file '{args.jsonfile}' is not a valid JSON file")
        return None

def print_json(jsondata):
        print(json.dumps(jsondata, indent=4))

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Path to JSON file")
        parser.add_argument('--jsonfile', nargs=1, dest='jsonfile', required=True, help="Path to the JSON file")

        #Parse arguments
        args = parser.parse_args()

        #Load JSON file
        jsondata = load_json(args) 
        if jsondata is None:
                print("Failed to process JSON input. Exiting")
                sys.exit(2)

        print_json(jsondata)
