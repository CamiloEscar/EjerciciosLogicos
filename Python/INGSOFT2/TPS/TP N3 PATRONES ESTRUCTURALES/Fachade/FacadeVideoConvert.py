from Render import Render
from VideoConvert import VideoConvert


class FacadeVideoConvert:

    def __init__(self) -> None:
        self.vConvert = VideoConvert()
        self.vRender = Render()

    def convertirVideoAOtroFormato(self, videoPath, formato) -> None:
        
        render = ""
        video = self.vConvert.convert(videoPath, formato)
        if video[0]:
            render = self.vRender.renderVideo(video[2])
            print("Video renderizado y convertido a ", formato)
        else:
            print('No se pudo convertir el video a ', formato)
            render = None

        return render