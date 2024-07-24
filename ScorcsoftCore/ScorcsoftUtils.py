import time
import json
from datetime import datetime
import ScorcsoftCore.config as config


def dateToStamp(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date_object = datetime.strptime(date_string, date_format)
    timestamp = datetime.timestamp(date_object)
    return timestamp


def calcInterval(start_date, end_date):
    date_format = '%Y-%m-%d %H:%M:%S'
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
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


def saveSetting():
    try:
        fp = open('./ScorcsoftCore/config.json', 'w')
        fp.write(json.dumps(config.Settings))
        fp.close()
    except:
        pass


def countdown():
    if 'end_time' not in config.Settings.keys():
        return config.errors['no time setup']

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    end = time.strftime(f'%Y-%m-%d {config.Settings["end_time"]}:00')

    if time.time() > config.Settings["end_time_stamp"]:
        if time.time() >= config.Settings['start_time_stamp']:  # 已经到第二天上班时间，重置计时器
            config.Settings['start_time_stamp'] = dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["start_time"]}:00'))
            config.Settings['end_time_stamp'] = dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["end_time"]}:00'))
            if config.Settings['start_time_stamp'] > config.Settings['end_time_stamp']:
                config.Settings['end_time_stamp'] += 86400
        else:
            return '00:00:00'

    return calcInterval(now, end)


def calcPercent():
    if time.time() > config.Settings["end_time_stamp"]:  # 当前时间大于下班时间，直接显示为100%
        return '100%'

    if time.time() < config.Settings["start_time_stamp"]:  # 当前时间小于上班时间，直接显示为0%
        return '0%'

    totalSeconds = int(config.Settings["end_time_stamp"] - config.Settings["start_time_stamp"])
    string = (time.time() - config.Settings["start_time_stamp"]) / totalSeconds * 100
    return '%.2f%%' % round(string, 2)
