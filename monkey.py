import os
import sys
import json

try:
    import rumps
    import PyQt5
except ModuleNotFoundError as e:
    print('run command to install module: ')
    if e.name == 'rumps':
        print('pip3 install rumps rumps')
    elif e.name == 'PyQt5':
        print('pip3 install rumps PyQt5')
    sys.exit(0)

import ScorcsoftCore.config as config

if sys.platform == 'darwin':
    import Mac.MacMonkey as MacMonkey
else:
    print('现在只能在Mac上使用，辣鸡Windows的还没来得及写，过几天再说！')
    sys.exit()

if os.path.isfile('config.json'):
    try:
        fp = open('config.json', 'r')
        config.Settings = json.loads(fp.read())
        fp.close()
        if 'countdown_note' not in config.Settings.keys():
            config.Settings['countdown_note'] = ''
        if 'start_time' not in config.Settings.keys():
            config.Settings['start_time'] = '09:00'
        if 'end_time' not in config.Settings.keys():
            config.Settings['end_time'] = '17:00'
        if 'percent_note' not in config.Settings.keys():
            config.Settings['percent_note'] = ''
        if 'percent_display' not in config.Settings.keys():
            config.Settings['percent_display'] = 1
        if 'wage_note' not in config.Settings.keys():
            config.Settings['wage_note'] = ''
        if 'wage_symbol' not in config.Settings.keys():
            config.Settings['wage_symbol'] = ''
        if 'wage' not in config.Settings.keys():
            config.Settings['wage'] = 0
        if 'wage_display' not in config.Settings.keys():
            config.Settings['wage_display'] = 1
    except:
        config.Settings = {"countdown_note": "", "start_time": "08:20", "end_time": "16:40", "percent_note": "",
                           "percent_display": 1, "wage_note": "", "wage_symbol": "", "wage": 0, "wage_display": 1}
        print('加载本地配置失败')
else:
    config.Settings = {"countdown_note": "", "start_time": "08:20", "end_time": "16:40", "percent_note": "",
                       "percent_display": 1, "wage_note": "", "wage_symbol": "", "wage": 0, "wage_display": 1}
    print('没有配置文件，请重新设置。')

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
    monkey = MacMonkey.MonkeyApp()
    monkey.run()
