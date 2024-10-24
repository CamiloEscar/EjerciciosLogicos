from ImpresorFrameHDMI import ImpresorFrameHDMI
from ImpresorFrameVGA import ImpresorFrameVGA
from ImpresorFrameDVI import ImpresorFrameDVI
from ImpresorFraneVGAAdapter import ImpresorFraneVGAAdapter
from ImpresorFraneDVIAdapter import ImpresorFraneDVIAdapter
from imprimirFrame import imprimirFrame


impresorHDMI = ImpresorFrameHDMI()
imprimirFrame(impresorHDMI, 'frame01')
print("\n")

print("Imprimir de frame VGA sin adaptarlo al conector hdmi\n")
impresorFrameVga = ImpresorFrameVGA()
impresorFrameVga.ImprimirFrame('frame01')
print("\n")

print("Imprimir de VGA a HDMI\n")
adapterVga = ImpresorFraneVGAAdapter()
imprimirFrame(adapterVga, 'frame01')

print("Imprimir de frame DVI sin adaptarlo al conector hdmi\n")
impresorFrameDvi = ImpresorFrameDVI()
impresorFrameDvi.ImprimirFrame('frame01')
print("\n")

print("Imprimir de DVI a HDMI\n")
adapterDvi = ImpresorFraneDVIAdapter()
imprimirFrame(adapterDvi, 'frame01')
print("\n")