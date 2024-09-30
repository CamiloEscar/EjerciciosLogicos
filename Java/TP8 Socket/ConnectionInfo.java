
/**
 * @author camilo
 *
 * Ejercicio 2
 * Realizar un programa que se conecte a un host y muestre informaci�n acerca de la conexi�n usando los
 * m�todos getInetAddress() y getPort().
 *
 * Para crear un programa en Java que se conecte a un host y muestre informaci�n acerca de la conexi�n
 * utilizando los m�todos getInetAddress() y getPort(), puedes utilizar la clase Socket del paquete java.net.
 */
import java.net.Socket;
import java.net.InetAddress;
import java.io.IOException;

public class ConnectionInfo {

    public static void main(String[] args) {
        String host = "www.google.com"; // Cambia el host a la direcci�n que desees

        try {
            // Obtiene la direcci�n IP a la que se ha conectado
            try ( // Intenta crear una conexi�n a la direcci�n y el puerto especificados
                    Socket socket = new Socket(host, 80)) {
                // Obtiene la direcci�n IP a la que se ha conectado
                InetAddress remoteAddress = socket.getInetAddress();
                // Obtiene el puerto al que se ha conectado
                int port = socket.getPort();
                // Muestra la informaci�n de la conexi�n
                System.out.println("Conectado a: " + remoteAddress);
                System.out.println("Puerto: " + port);
                // Cierra la conexi�n
            }
        } catch (IOException e) {
            System.err.println("Error al conectar al host: " + e.getMessage());
        }
    }
}

/*
En este programa, primero especificas el host al que deseas conectarte en la variable host. 
Luego, en el bloque try, intentas crear una conexi�n a ese host en el puerto 80 
(en el ejemplo, se usa el puerto 80 com�nmente utilizado para HTTP). 
Luego, utilizas los m�todos getInetAddress() y getPort() para obtener la direcci�n IP y 
el puerto al que se ha conectado el socket. Finalmente, muestras esta informaci�n y cierras la conexi�n.

Para ejecutar el programa, sigue los pasos mencionados en la respuesta anterior, 
que incluyen compilar y ejecutar el programa en la l�nea de comandos. 
Aseg�rate de reemplazar "www.google.com" con la direcci�n del host al que deseas conectarte.
*/
