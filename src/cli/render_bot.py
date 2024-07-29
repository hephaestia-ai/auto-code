import argparse
import os
from auto_code.render_bot import CodeRefinementBot


def main():
    """Create new bots."""
    parser = argparse.ArgumentParser(description="Bot creation CLI Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Front end focused refinement
    parser_front_end = subparsers.add_parser('create')
    
    parser_front_end.add_argument('--bot_name', type=str, help='Pass name of bot to be created')

    args = parser.parse_args()

    code_refinement_bot = CodeRefinementBot()

    if args.command == 'create':
        code_refinement_bot.create_bot_file(args.bot_name)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
