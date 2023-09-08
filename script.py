"""
this script opens an excel file, in the pre-specified path, and parses it.
"""
import pandas as pd
from datetime import datetime

# Now 'df' contains the data from your Excel file

def parse_bday(df):
    # Extract the month, day, and year
    df['month'] = df['Birthday'].str[:2]
    df['day'] = df['Birthday'].str[2:4]
    df['year'] = '2000'
    new_df = df[['month', 'day', 'year']]; new_df
    # convert birthday dates to the appropriate format. NaT if previously NaN
    df['Birthday'] = pd.to_datetime(new_df, errors='coerce')
    return df


def bdays_this_month(df):
    """
    assumes the 'Birthday' column is formated as a datetime object. returns dataframe
    """
    current_date = datetime.now()
    current_month = current_date.month

    same_month_rows = df[df['Birthday'].dt.month == current_month]
    month_data = same_month_rows[["First Name", "Last Name", "day", "month"]]
    return month_data


def names_str(df):
    return ', '.join(list(df["First Name"]))
