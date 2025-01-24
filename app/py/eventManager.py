from syllable_separator_hu import  hyphenation


class eventManager:
    def __init__(self):
        self.actions = {
            "hello": self.onHello(),
            "exit": self.onExit(),
            "quit": self.onExit(),
            "wic": self.wicMode(),
            "sep": self.separatorMode(),
            "separate": self.separatorMode(),
            "separator": self.separatorMode()
        }

    def getAction(self, userAction):
        return self.actions.get(userAction)

    def onHello(self):
        print("Hello, there!")

    def wicMode(self):
        # run.py.start()
        pass

    def separatorMode(self):
        word = input("Kerem adja meg az elvalasztando szot!")
        hyphenation.hyphenate(word)

    @staticmethod
    def onExit():
        exit()