"""
This script generates a random date between two given dates and prints it.
If the randomly chosen date falls on a Monday, a message is displayed instead.
"""

from datetime import datetime as dt, timedelta
import random


def no_vinnigrete(start_date, end_date):
    """
        Generates a random date between start_date and end_date.
        If the date falls on a Monday, prints a message instead.

        :param start_date: Start date in 'YYYY-MM-DD' format.
        :param end_date: End date in 'YYYY-MM-DD' format.
        """
    try:

    # Convert strings to datetime objects
        start = dt.strptime(start_date, '%Y-%m-%d')
        end = dt.strptime(end_date, '%Y-%m-%d')

    # Generate a random date
        delta = end - start
        random_days = random.randint(0, delta.days)
        random_date = start + timedelta(days=random_days)

        if random_date.weekday() == 0:  # 0 = Monday
            print("Ain't gettin' no vinaigrette today :(")
        else:
            print(random_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print("Please enter a valid date ", e)

if __name__ == '__main__':
    print(no_vinnigrete("2024-01-01", "2024-12-31"))
