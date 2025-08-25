import json
import sys

def dump_json(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <json-file>", file=sys.stderr)
        sys.exit(1)
    dump_json(sys.argv[1])

