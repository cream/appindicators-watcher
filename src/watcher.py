import cream
from cream.contrib.appindicators.watcher import StatusNotifierWatcher

class WatcherModule(cream.Module, StatusNotifierWatcher):
    def __init__(self):
        cream.Module.__init__(self)
        StatusNotifierWatcher.__init__(self)

if __name__ == '__main__':
    watcher = WatcherModule()
    watcher.main()
