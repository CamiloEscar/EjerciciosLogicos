
import java.net.*;
import java.io.*;

public class EjPuertos_tcp {

    public static void main(String[] args) {

        Socket so_check_port;
        String host = "www.google.com.ar";

        try {
            so_check_port = new Socket(host, 80);
            System.out.println("conectado:" + so_check_port.getInetAddress());
            System.out.println("port :" + so_check_port.getPort());
        } // try
        catch (UnknownHostException e) {
            System.out.println(e);
        } // catch
        catch (IOException e) {
            System.out.println(e);
        } // catch
    }
} // Puertos_tcp

/*
Importas las clases necesarias del paquete java.net y java.io.

Comienzas la declaraci�n de la clase Puertos_tcp.

Inicias el m�todo main, que es el punto de entrada de la aplicaci�n.

Declaras una variable so_check_port para representar el socket que intentar� establecer la conexi�n.

Especificas el nombre del host al que te quieres conectar, en este caso, "www.google.com.ar".

Comienzas un bloque try para manejar las excepciones que pueden ocurrir al intentar establecer la conexi�n.

Intentas crear un nuevo objeto de tipo Socket con el nombre del host y el puerto 80. Esto intentar� establecer una conexi�n TCP con el host.

Imprimes en la consola la direcci�n IP a la que se ha conectado el socket utilizando getInetAddress().

Imprimes en la consola el puerto al que se ha conectado el socket utilizando getPort().

16-18. Capturas la excepci�n UnknownHostException, que se lanza si no se puede resolver el nombre de host, e imprimes el error.

19-21. Capturas la excepci�n IOException, que se lanza si ocurre alg�n error de E/S durante la conexi�n, e imprimes el error.

Cierras el bloque main.
En resumen, este programa intenta establecer una conexi�n con el host "www.google.com.ar" en el puerto 80 y muestra en la consola la direcci�n IP 
a la que se ha conectado y el puerto utilizado. Ten en cuenta que este es un ejemplo b�sico de conexi�n TCP y que en una aplicaci�n real, 
se pueden realizar m�s operaciones como el env�o y recepci�n de datos.
*/
