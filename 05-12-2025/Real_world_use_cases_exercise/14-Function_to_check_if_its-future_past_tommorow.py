from datetime import datetime,date,timedelta
def past_present_future(given_date):
    if date.today()>given_date:
        print("This Day is in past")
    elif date.today()<given_date:
        print("This Day is in future")
    elif date.today()==given_date:
        print("Its Today")

past_present_future(date(2026,3,12))