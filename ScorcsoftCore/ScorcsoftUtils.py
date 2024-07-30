import time
import json
from datetime import datetime
import ScorcsoftCore.config as config


def dateToStamp(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date_object = datetime.strptime(date_string, date_format)
    timestamp = datetime.timestamp(date_object)
    return timestamp


def saveSetting():
    try:
        fp = open('config.json', 'w')
        fp.write(json.dumps(config.Settings))
        fp.close()
    except:
        pass


def countdown(startTimeStamp, endTimeStamp, now):
    if startTimeStamp < now < endTimeStamp:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        end = time.strftime(f'%Y-%m-%d {config.Settings["end_time"]}:00')
        date_format = '%Y-%m-%d %H:%M:%S'
        start = datetime.strptime(now, date_format)
        end = datetime.strptime(end, date_format)
        delta = end - start
        days = delta.days
        seconds = delta.seconds
        minutes = seconds // 60
        hours = minutes // 60
        minutes %= 60
        seconds %= 60

        result = config.Settings['countdown_note']
        if days > 0:
            result += f'{days}:'
        result += '%02d:%02d:%02d' % (hours, minutes, seconds)
        return result

    return f'{config.Settings["countdown_note"]}00:00:00'


def calcPercent(startTimeStamp, endTimeStamp, now):
    if now > endTimeStamp:  # 当前时间大于下班时间，直接显示为100%
        return ' | 100%'

    if now < startTimeStamp:  # 当前时间小于上班时间，直接显示为0%
        return ' | 0%'

    totalSeconds = int(endTimeStamp - startTimeStamp)
    p = (time.time() - startTimeStamp) / totalSeconds * 100
    return f' | {config.Settings["percent_note"]}%.2f%%' % round(p, 2)


def calcWage(startTimeStamp, endTimeStamp, now, wage):
    if isinstance(wage, int) and wage > 0:
        title = f' | {config.Settings["wage_note"]}{config.Settings["wage_symbol"]}'
        if now > endTimeStamp:  # 当前时间大于下班时间，直接显示为100%
            title += f'%.2f' % round(float(config.Settings['wage']), 2)
        elif now < startTimeStamp:
            title += '0.00'
        else:
            nowWage = wage / (endTimeStamp - startTimeStamp) * (now - startTimeStamp)

            title += '%.2f' % round(nowWage, 2)
        return title
    else:
        return ' | 日薪不正确'
