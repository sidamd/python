import json
import sys
import argparse
import subprocess
import shlex

CMD='cmd'
CMDS='cmds'
PIPE2CMDS='pipe2cmds'


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

def run_one_command(cmd1):
    p1 = subprocess.run(shlex.split(cmd1), capture_output=True, text=True)
    return p1.stdout

# take two command arrays
def run_pipe_cmds(cmd1, cmd2):
    p1 = subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(shlex.split(cmd2), stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    return output.decode('utf-8')


def print_json(jsondata):
        print(json.dumps(jsondata, indent=4))

def print_section(jsondata, section):
    """Print only a specific section of the JSON file."""
    if section in jsondata:
        print(json.dumps(jsondata[section], indent=4))
    else:
        print(f"Section '{section}' not found in JSON file.")

def list_section(jsondata, section):
    """List keys for a specific section."""
    if CMD in jsondata[section]:
         print(jsondata[section][CMD])
         return

    if CMDS in jsondata[section]:
         for cmd in jsondata[section][CMDS]:
             print(cmd)
 
    if PIPE2CMDS in jsondata[section]:
         print(jsondata[section][PIPE2CMDS][0], "|", jsondata[section][PIPE2CMDS][1])

def run_all_sections(jsondata):
    for section in jsondata.keys():
        if CMD in jsondata[section]:
            print(run_one_command(jsondata[section][CMD]))
        if CMDS in jsondata[section]:
            for cmd in jsondata[section][CMDS]:
                print(run_one_command(cmd))
        if PIPE2CMDS in jsondata[section]:
            print(run_pipe_cmds(jsondata[section][PIPE2CMDS][0], jsondata[section][PIPE2CMDS][1]))

def run_section(jsondata, section):
    if CMD in jsondata[section]:
         print(run_one_command(jsondata[section][CMD]))
    if CMDS in jsondata[section]:
         for cmd in jsondata[section][CMDS]:
             print(run_one_command(cmd))
    if PIPE2CMDS in jsondata[section]:
         print(run_pipe_cmds(jsondata[section][PIPE2CMDS][0], jsondata[section][PIPE2CMDS][1]))

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Path to JSON file")
        parser.add_argument('--jsonfile', nargs=1, dest='jsonfile', required=True, help="Path to the JSON file")
        parser.add_argument('--section', nargs=1, dest='section', help="Print only a specific section of the JSON")

        #Parse arguments
        args = parser.parse_args()

        #Load JSON file
        jsondata = load_json(args) 
        if jsondata is None:
                print("Failed to process JSON input. Exiting")
                sys.exit(2)

        print_json(jsondata)

            # Print section if requested, otherwise dump full JSON
        if args.section is None:
                print(args.section)
                run_all_sections(jsondata)
        else:
                run_section(jsondata, args.section[0])

