import time
import rumps
import ScorcsoftCore.config as config
import ScorcsoftCore.settings as settings
import ScorcsoftCore.ScorcsoftUtils as scorcsoftUtils


class NSApplicationDelegate:
    def applicationSupportsSecureRestorableState(self, app):
        print(app)
        return True

class MonkeyApp(rumps.App):
    def __init__(self):
        if len(config.Settings) == 0:
            self.title = config.errors['no time setup']
        super(MonkeyApp, self).__init__('HW保留节目2024限定版')
        self.menu = [
            rumps.MenuItem(title='显示时间百分比', callback=self.percentSwitch),
            rumps.MenuItem(title='显示日薪', callback=self.wageSwitch)
        ]

        self.update_status()
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

        startTimeStamp = scorcsoftUtils.dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["start_time"]}:01'))
        endTimeStamp = scorcsoftUtils.dateToStamp(time.strftime(f'%Y-%m-%d {config.Settings["end_time"]}:00'))
        if endTimeStamp <= startTimeStamp:
            endTimeStamp += 86400
        now = time.time()

        title = scorcsoftUtils.countdown(startTimeStamp, endTimeStamp, now)

        if config.Settings['percent_display'] == 0:
            title += scorcsoftUtils.calcPercent(startTimeStamp, endTimeStamp, now)

        if config.Settings['wage_display'] == 0:
            title += scorcsoftUtils.calcWage(startTimeStamp, endTimeStamp, now, config.Settings['wage'])

        self.title = title
        self.update_status()

    def update_status(self):
        items = self.menu.items()
        items[0][1].state = not (config.Settings['percent_display'] == 1)
        items[1][1].state = not (config.Settings['wage_display'] == 1)
