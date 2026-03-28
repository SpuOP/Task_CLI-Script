import argparse 
import sys 
parser = argparse.ArgumentParser()
parser.add_argument("task", type=str, nargs="?", help="Task to Add")
args = parser.parse_args()

if len (sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.task:
      print(f"Task added: {args.task} added with ID of 1")

