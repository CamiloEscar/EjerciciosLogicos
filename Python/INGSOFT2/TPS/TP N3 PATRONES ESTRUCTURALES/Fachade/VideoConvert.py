import string


class VideoConvert():

    def __getFormat(self, videoPath):
        k = 0
        for i in range(1, len(videoPath)):
            if(videoPath[-i] == '.'):
                k = i
                break
        
        k -= 1

        return videoPath[len(videoPath) - k: len(videoPath)]

    def convert(self, videoPath, format):
        formats = ["mp4", "avi", "wav"]
        originalFormat = self.__getFormat(videoPath)
        if((originalFormat in ['h264', 'h265'])
            and (format in formats)):
            print('convirtiendo el video ', videoPath, ' a ', format)
            print('video convertido a ', format)
            return True, 'Conversion terminada', (videoPath[0: (len(videoPath) - len(originalFormat))] + format)
        
        return False, 'Error al convertir el video', videoPath
