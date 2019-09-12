import pytz
from datetime import datetime

def get_datetime_with_timezone():
    return pytz.utc.localize(datetime.utcnow())