import argparse
import importlib
import traceback

def setup_argparse_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a specific yar/day/part of the advent calendar.")
    parser.add_argument(
        "year",
        type=int,
        help="Advent Calendar year, e.g. 2024",
    )
    parser.add_argument(
        "day",
        type=int,
        help="Day to run, e.g. 2",
    )
    parser.add_argument(
        "part",
        type=int,
        choices=[1,2],
        help="Which part of the day to run, only should be part 1 or 2."
    )
    return parser

def main():
    parser = setup_argparse_parser()
    args = parser.parse_args()
    advent_year_day_string = f"Advent of Code year={args.year}, day={args.day}"

    try:
        # Dynamically import the chosen script
        script_module = importlib.import_module(f"y{args.year}.day_{args.day}")

        # Check if the corresponding part is available in this year/day
        if hasattr(script_module, f"part_{args.part}"):
            # Call the part selected
            if args.part == 1:
                script_module.part_1()
            else:
                script_module.part_2()
        else:
            print(f"Error: {advent_year_day_string} doesn't have a part_{args.part} function.")
    except:
        print(f"Error: Could not import for {advent_year_day_string}")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
