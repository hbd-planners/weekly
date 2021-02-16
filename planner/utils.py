from datetime import datetime, date, timedelta


def get_current_week_range(day=date.today()):
    """Function to get current week start day end end day
    :returns: string of current week range

    """
    weekday = date.weekday(day)
    monday = day - timedelta(days=weekday)
    sunday = day + timedelta(days=6-weekday)
    
    monday_format = date.strftime(monday, format="%a, %d-%m-%Y")
    sunday_format = date.strftime(sunday, format="%a, %d-%m-%Y")
    
    return f"{monday_format} - {sunday_format}"
