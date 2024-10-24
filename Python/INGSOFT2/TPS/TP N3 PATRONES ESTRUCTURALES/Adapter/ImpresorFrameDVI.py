class ImpresorFrameDVI:
    def getResolucion(self) -> str:
        return "1080"
    
    def ImprimirFrame(self, frame) -> None:
        print(frame, " ", self.getResolucion())