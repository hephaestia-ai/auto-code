import argparse
import os
import json
from src.auto_code.auto_code import AutoCode

TEMP_FILE = 'temp_files.json'

def main():
    """Main entry point for the Auto Code CLI Tool."""
    parser = argparse.ArgumentParser(description="Auto Code CLI Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_get_files = subparsers.add_parser('refine', help='Get list of files in directory with given extension, sends to refinery for updates')
    parser_get_files.add_argument('dir', type=str, help='Directory containing files')
    parser_get_files.add_argument('ext', type=str, help='File extension to load')

    args = parser.parse_args()

    auto_code = AutoCode()

    if args.command == 'refine':
        assert os.path.isdir(args.dir), f"Error: The specified directory '{args.dir}' does not exist."
        file_list = auto_code.get_files(args.dir, args.ext)
        auto_code.refine(file_list)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()