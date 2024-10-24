from SingletonMeta import SingletonMeta


class SingletonVideoDigital(metaclass=SingletonMeta):

    def getid(self):
        return "Video Digital"
        
    def getCuit(self):
        return "30-71469658-7"