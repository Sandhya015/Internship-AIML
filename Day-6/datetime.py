from datetime import datetime


def get_current_datetime()->dict:
    now = datetime.now()

    result ={
        "current_date":now.date(),
        "current_time":now.time(),
        "formated_datetime":now.strftime("%Y-%m-%d %H:%M:%S")


    }
    return result