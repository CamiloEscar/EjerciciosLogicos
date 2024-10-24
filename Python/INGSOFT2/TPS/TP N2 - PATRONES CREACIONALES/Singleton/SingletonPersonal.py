from SingletonMeta import SingletonMeta


class SingletonPersonal(metaclass=SingletonMeta):

    def getid(self):
        return "Personal"
        
    def getCuit(self):
        return "30-63945373-8"