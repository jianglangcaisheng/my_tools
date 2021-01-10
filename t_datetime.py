import datetime


def timestamp2str(timestamp, fmt="%y%m%d-%H%M%S", GMT=0):
    time = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(hours=GMT)
    res = time.strftime(fmt)
    return res


def date2milisecond(date_str, GMT=0):
    time = datetime.datetime.strptime(date_str, "%y%m%d") - datetime.timedelta(hours=GMT)
    res = int(time.timestamp() * 1000)
    return res


def get_current_timestr(fmt="%Y-%m-%d %H:%M:%S", GMT=8):
    timestr = (datetime.datetime.now() + datetime.timedelta(hours=GMT)).strftime(fmt)
    return timestr


def print_time_info(print_str):
    print(get_current_timestr() + ", " + print_str)


if __name__ == "__main__":
    if 0:
        res = timestamp2str(datetime.datetime.now().timestamp())
        print(res)

    if 1:
        print_time_info("test. ")
