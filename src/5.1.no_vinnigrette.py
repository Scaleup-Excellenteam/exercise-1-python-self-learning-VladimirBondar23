from datetime import datetime as dt, timedelta
import random


def no_vinnigrete(start_date, end_date):

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
    print(no_vinnigrete())