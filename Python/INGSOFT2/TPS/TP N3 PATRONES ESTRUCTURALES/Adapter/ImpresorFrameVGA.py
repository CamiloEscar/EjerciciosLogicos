class ImpresorFrameVGA:
    def getResolucion(self) -> str:
        return "1080", "1920"
    
    def ImprimirFrame(self, frame) -> None:
        print(frame, " ", self.getResolucion())