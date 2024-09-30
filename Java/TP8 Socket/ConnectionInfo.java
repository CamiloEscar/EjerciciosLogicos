
/**
 * @author camilo
 *
 * Ejercicio 2
 * Realizar un programa que se conecte a un host y muestre información acerca de la conexión usando los
 * métodos getInetAddress() y getPort().
 *
 * Para crear un programa en Java que se conecte a un host y muestre información acerca de la conexión
 * utilizando los métodos getInetAddress() y getPort(), puedes utilizar la clase Socket del paquete java.net.
 */
import java.net.Socket;
import java.net.InetAddress;
import java.io.IOException;

public class ConnectionInfo {

    public static void main(String[] args) {
        String host = "www.google.com"; // Cambia el host a la dirección que desees

        try {
            // Obtiene la dirección IP a la que se ha conectado
            try ( // Intenta crear una conexión a la dirección y el puerto especificados
                    Socket socket = new Socket(host, 80)) {
                // Obtiene la dirección IP a la que se ha conectado
                InetAddress remoteAddress = socket.getInetAddress();
                // Obtiene el puerto al que se ha conectado
                int port = socket.getPort();
                // Muestra la información de la conexión
                System.out.println("Conectado a: " + remoteAddress);
                System.out.println("Puerto: " + port);
                // Cierra la conexión
            }
        } catch (IOException e) {
            System.err.println("Error al conectar al host: " + e.getMessage());
        }
    }
}

/*
En este programa, primero especificas el host al que deseas conectarte en la variable host. 
Luego, en el bloque try, intentas crear una conexión a ese host en el puerto 80 
(en el ejemplo, se usa el puerto 80 comúnmente utilizado para HTTP). 
Luego, utilizas los métodos getInetAddress() y getPort() para obtener la dirección IP y 
el puerto al que se ha conectado el socket. Finalmente, muestras esta información y cierras la conexión.

Para ejecutar el programa, sigue los pasos mencionados en la respuesta anterior, 
que incluyen compilar y ejecutar el programa en la línea de comandos. 
Asegúrate de reemplazar "www.google.com" con la dirección del host al que deseas conectarte.
*/
