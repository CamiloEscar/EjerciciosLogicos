# Implementar un remito que tenga en cuenta distribución por
# correo, por mensajería o por portal de ventas.
from Factory import client_code
from RemitoCorreo import RemitoCorreo
from RemitoMensajeria import RemitoMensajeria
from RemitoPortalVentas import RemitoPortalVentas

client_code(RemitoCorreo())
client_code(RemitoMensajeria())
client_code(RemitoPortalVentas())