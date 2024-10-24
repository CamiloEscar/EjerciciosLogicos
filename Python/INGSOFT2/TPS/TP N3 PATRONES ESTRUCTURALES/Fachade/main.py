from FacadeVideoConvert import FacadeVideoConvert

def client_code(facade: FacadeVideoConvert):
    
    pat = "C/Usuarios/Gonzalo/shakira.h264"
    formato = "mp4"
    video = facade.convertirVideoAOtroFormato(pat, formato)

    print(video[1])

facade = FacadeVideoConvert()
client_code(facade)


