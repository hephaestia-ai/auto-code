import argparse
import os
import json
from src.auto_code.auto_code import AutoCode

TEMP_FILE = 'temp_files.json'

def main():
    """Main entry point for the Auto Code CLI Tool."""
    parser = argparse.ArgumentParser(description="Auto Code CLI Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Get list of files
    parser_get_files = subparsers.add_parser('get_files', help='Get list of files in directory with given extension')
    parser_get_files.add_argument('dir', type=str, help='Directory containing files')
    parser_get_files.add_argument('ext', type=str, help='File extension to load')

    # Refine files
    parser_refine = subparsers.add_parser('refine', help='Refine specified files')
    parser_refine.add_argument('file_name', type=str, help='Name of the file to refine')

    args = parser.parse_args()

    auto_code = AutoCode()

    if args.command == 'get_files':
        assert os.path.isdir(args.dir), f"Error: The specified directory '{args.dir}' does not exist."
        file_list = auto_code.get_files(args.dir, args.ext)
        with open(TEMP_FILE, 'w') as temp_file:
            json.dump(file_list, temp_file)
        print(f"Files list saved to {TEMP_FILE}")

    elif args.command == 'refine':
        if not os.path.exists(TEMP_FILE):
            print(f"Error: {TEMP_FILE} not found. Run 'get_files' command first.")
            return
        
        with open(TEMP_FILE, 'r') as temp_file:
            file_list = json.load(temp_file)
        
        assert isinstance(file_list, list), "Error: The saved file list is not in the expected format."
        
        if args.file_name in file_list:
            auto_code.process_files([args.file_name])
            print(f"Refined file: {args.file_name}")
        else:
            print(f"Error: {args.file_name} not found in the saved file list.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()