import argparse
import os
from auto_code.scripting_bot import ScriptingBot


def main():
    """Main entry point for the Auto Code CLI Tool."""
    parser = argparse.ArgumentParser(description="Auto Code CLI Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # General python refinement
    parser_refine = subparsers.add_parser('refine', 
                            help='Get list of files in directory with   \
                                    given extension or a single file, sends \
                                    to refinery for updates')
    
    parser_refine.add_argument('--dir', type=str, help='Directory containing files')
    parser_refine.add_argument('--ext', type=str, help='File extension to load')
    parser_refine.add_argument('--file', type=str, help='Full file path')

    args = parser.parse_args()

    auto_code = ScriptingBot()

    if args.command == 'refine':

        if args.file:
            assert os.path.isfile(args.file), f"Error: The specified file '{args.file}' does not exist."
            file_list = [args.file]
        else:
            assert os.path.isdir(args.dir), f"Error: The specified directory '{args.dir}' does not exist."
            assert args.ext, "Error: File extension must be provided when specifying a directory."
            file_list = auto_code.get_files(args.dir, args.ext)
        auto_code.refine(file_list)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
