
import argparse
import pandas as pd
from datetime import datetime
import script
from hidden_vars import file_path

# Use the read_excel function to read the Excel file into a DataFrame


# parsed_df = script.parse_bday(df)
# this_months_bdays = script.bdays_this_month(parsed_df)
# names_bdays = script.names_str(this_months_bdays)


def main():
    parser = argparse.ArgumentParser(description="Birthday information CLI")
    parser.add_argument(
        "--keyword", choices=["bdays", "birthdays"], help="Enter 'bdays' or 'birthdays'")

    args = parser.parse_args()

    if args.keyword == "bdays" or args.keyword == "birthdays":
        # Call the functions based on the keyword
        df = pd.read_excel(file_path)
        parsed_df = script.parse_bday(df)
        this_months_bdays = script.bdays_this_month(parsed_df)
        names_bdays = script.names_str(this_months_bdays)

        # Print the last variable
        print(names_bdays + " were born this month.")
    else:
        print("Please enter a valid keyword: 'bdays' or 'birthdays'")


if __name__ == "__main__":
    main()
