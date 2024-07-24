import os
import sys
import time
import json
import ScorcsoftCore.config as config
import ScorcsoftCore.ScorcsoftUtils as scorcsoftUtils


try:
    import rumps
except ModuleNotFoundError:
    print('run command to install rumps: ')
    print('pip3 install rumps')
    sys.exit(0)


if sys.platform == 'darwin':
    import Mac.MacMonkey as MacMonkey
else:
    print('现在只能在Mac上使用，辣鸡Windows的还没来得及写，过几天再说！')


if os.path.isfile('./ScorcsoftCore/config.json'):
    try:
        fp = open('./ScorcsoftCore/config.json', 'r')
        config.Settings = json.loads(fp.read())
        config.Settings['start_time_stamp'] = scorcsoftUtils.dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["start_time"]}:00'))
        config.Settings['end_time_stamp'] = scorcsoftUtils.dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["end_time"]}:00'))
        fp.close()
    except:
        pass

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
