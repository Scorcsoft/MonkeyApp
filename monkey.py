import os
import sys
import json
try:
    import rumps
    import PyQt5
except ModuleNotFoundError:
    print('run command to install rumps and PyQt5: ')
    print('pip3 install rumps PyQt5')
    sys.exit(0)
import ScorcsoftCore.config as config


if sys.platform == 'darwin':
    import Mac.MacMonkey as MacMonkey
else:
    print('现在只能在Mac上使用，辣鸡Windows的还没来得及写，过几天再说！')


if os.path.isfile('config.json'):
    try:
        fp = open('config.json', 'r')
        config.Settings = json.loads(fp.read())
        fp.close()
    except:
        print('加载本地配置失败')
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
