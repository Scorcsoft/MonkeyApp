import sys
import time
import threading
import ScorcsoftCore.config as config
import ScorcsoftCore.settings as settings
import ScorcsoftCore.ScorcsoftUtils as scorcsoftUtils
try:
    import rumps
except ModuleNotFoundError:
    print('run command to install rumps: ')
    print('pip3 install rumps')
    sys.exit(0)


class MonkeyApp(rumps.App):
    def __init__(self):
        if len(config.Settings) == 0:
            self.title = config.errors['no time setup']
        if 'wage_display' in config.Settings.keys():
            if config.Settings['wage_display'] == 0:
                wageDisplay = True
            else:
                wageDisplay = False
        else:
            wageDisplay = False
        if 'percent_display' in config.Settings.keys():
            if config.Settings['percent_display'] == 0:
                percentDisplay = True
            else:
                percentDisplay = False
        else:
            percentDisplay = False

        super(MonkeyApp, self).__init__('HW保留节目2024限定版')
        self.menu = [
            rumps.MenuItem(title='显示时间百分比', callback=self.percentSwitch),
            rumps.MenuItem(title='显示日薪', callback=self.wageSwitch)
        ]

        rumps.Timer(self.update, 1).start()

    def percentSwitch(self, sender):
        if len(config.Settings) == 0:
            return
        if sender.state:
            config.Settings['percent_display'] = 1
        else:
            config.Settings['percent_display'] = 0
        sender.state = not sender.state
        scorcsoftUtils.saveSetting()

    def wageSwitch(self, sender):
        if len(config.Settings) == 0:
            return
        if sender.state:
            config.Settings['wage_display'] = 1
        else:
            config.Settings['wage_display'] = 0
        sender.state = not sender.state
        scorcsoftUtils.saveSetting()

    @rumps.clicked('设置')
    def setStartTime(self, sender):
        settings.setting()

    def update(self, sender):
        if len(config.Settings) == 0:
            self.title = config.errors['no time setup']
            return

        title = scorcsoftUtils.countdown()

        if config.Settings['percent_display'] == 0:
            title += f' | {config.Settings["percent_note"]}{scorcsoftUtils.calcPercent()}'

        if config.Settings['wage_display'] == 0:
            if isinstance(config.Settings['wage'], int) and config.Settings['wage'] > 0:
                if time.time() > config.Settings["end_time_stamp"]:  # 当前时间大于下班时间，直接显示为100%
                    title += ' | %.2f' % round(float(config.Settings['wage']), 2)
                else:
                    wage = config.Settings['wage'] / (config.Settings['end_time_stamp'] - config.Settings['start_time_stamp']) * (
                            time.time() - config.Settings['start_time_stamp'])
                    title += f' | {config.Settings["wage_note"]}{config.Settings["wage_symbol"]}'
                    title += '%.2f' % round(wage, 2)
            else:
                rumps.alert("日薪设置错误，需要设置为大于0的整数")
                config.Settings['wage_display'] = False

        self.title = title


