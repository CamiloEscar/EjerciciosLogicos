
/**
 * @author camilo
 * Socket TCP Servidor
 * El funcionamiento del socket servidor se puede sintetizar en los siguientes pasos :
 * 1. Creación de un servidor con el método ServerSocket(), atendiendo en un puerto.
 * 2. El servidor escucha los intentos de pedido de conexión en el puerto usando el método accept(),
 * crea una conexión retornando un objeto socket conectado al socket cliente.
 * 3. Se leen datos en el InputStream o se escriben datos en el OutputStream con los métodos
 * getInputStream() o getOutputSteam() para comunicarse con el cliente.
 * 4. El servidor y el cliente interactúan de acuerdo al protocolo que se este utilizando, hasta que se
 * cierra la conexión.
 * 5. El cliente o el servidor cierran la conexión.
 * 6. Se retorna al paso 2, esperando una nueva conexión.
 */
import java.io.*;
import java.net.*;

public class TCPServer {

    public static void main(String[] args) {
        int port = 12345; // Puerto en el que el servidor estará escuchando

        try {
            // Crear un ServerSocket que escuche en el puerto especificado
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("El servidor está escuchando en el puerto " + port);

            while (true) {
                try ( // Esperar y aceptar una conexión entrante
                        Socket clientSocket = serverSocket.accept()) {
                    System.out.println("Cliente conectado desde " + clientSocket.getInetAddress());
                    // Obtener flujos de entrada y salida para comunicarse con el cliente
                    DataInputStream inputStream = new DataInputStream(clientSocket.getInputStream());
                    PrintStream outputStream = new PrintStream(clientSocket.getOutputStream());
                    // Leer datos del cliente
                    String clientData = inputStream.readLine();
                    System.out.println("Cliente dice: " + clientData);
                    // Enviar una respuesta al cliente
                    String response = "Hola, soy el servidor. Recibí tu mensaje: " + clientData;
                    outputStream.println(response);
                    // Cerrar la conexión con el cliente
                }
                System.out.println("Conexión con el cliente cerrada");
            }
        } catch (IOException e) {
            System.err.println("Error en el servidor: " + e.getMessage());
        }
    }
}

/*
1- Creamos un ServerSocket en el puerto especificado (12345 en este caso) para que el servidor pueda escuchar conexiones entrantes.
2- En un bucle infinito, el servidor espera y acepta conexiones entrantes mediante el método accept(). Cuando se establece una conexión, creamos un objeto Socket para manejar la comunicación con el cliente.
3- Obtenemos flujos de entrada y salida (DataInputStream y PrintStream) para comunicarnos con el cliente.
4- Leemos datos del cliente utilizando inputStream y enviamos una respuesta utilizando outputStream.
5- Cerramos la conexión con el cliente.
6- El servidor vuelve al paso 2 para esperar una nueva conexión.
*/
