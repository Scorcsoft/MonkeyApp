import sys
import time
from datetime import datetime
try:
    import rumps
except ModuleNotFoundError:
    print('run command to install rumps: ')
    print('pip3 install rumps')
    sys.exit(0)


if sys.platform != 'darwin':
    print('only support MacOS!')
    sys.exit(0)


CONFIG = {
    'start_time': '08:20',  # 上班时间
    'end_time': '16:30',  # 下班时间
    'percent': True,  # 是否显示已摸鱼时间百分比
}


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

    result = ''
    if days > 0:
        result += f'{days}:'
    result += '%02d:%02d:%02d' % (hours, minutes, seconds)

    return result


def countdown():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    end = time.strftime(f'%Y-%m-%d {CONFIG["end_time"]}:00')

    if time.time() > CONFIG["end_time_stamp"]:
        return '00:00:00'

    return calcInterval(now, end)


def calcPercent():
    if time.time() > CONFIG["end_time_stamp"]:  # 当前时间大于下班时间，直接显示为100%
        return '100%'

    if time.time() < CONFIG["start_time_stamp"]:  # 当前时间小于上班时间，直接显示为0%
        return '0%'

    totalSeconds = int(CONFIG["end_time_stamp"] - CONFIG["start_time_stamp"])
    string = (time.time() - CONFIG["start_time_stamp"]) / totalSeconds * 100
    return '%.2f%%' % round(string, 2)


class MonkeyApp(rumps.App):
    def __init__(self):
        try:
            CONFIG['start_time_stamp'] = dateToStamp(time.strftime(f'%Y-%m-%d {CONFIG["start_time"]}:00'))
            CONFIG['end_time_stamp'] = dateToStamp(time.strftime(f'%Y-%m-%d {CONFIG["end_time"]}:00'))
        except:
            print('上下班时间不正确，请修改')
            sys.exit(0)

        super(MonkeyApp, self).__init__("HW保留节目2024限定版")
        self.title = ''
        rumps.Timer(self.update, 1).start()

    def update(self, sender):
        title = countdown()
        if CONFIG['percent']:
            title += f' | {calcPercent()}'
        self.title = title


monkeyASCII = r'''
            __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. \
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
        '._ '-=-' _.'
           '~---~'
'''

if __name__ == '__main__':
    print(monkeyASCII)
    monkey = MonkeyApp()
    monkey.run()
