from datetime import datetime, timedelta

GIGA_SEC = 10**9 # expressed in s

def add(dt: datetime):
    #
    # if dt.year < 1970:
    #    ts = (dt.astimezone(timezone.utc)- datetime(dt.year, 1, 1, tzinfo=timezone.utc)).total_seconds()
    # else: ts = dt.timestamp() + seconds=GIGA_SEC
    # return datetime.fromtimestamp(nts)
    #
    return dt + timedelta(seconds=GIGA_SEC)
