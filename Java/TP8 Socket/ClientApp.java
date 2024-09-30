
/**
 * @author camilo
 *
 * Ejercicio 7
 * Desarrollar una aplicación para enviar mensajes entre maquinas usando Sockets cliente y servidor
 */
import java.io.*;
import java.net.*;

public class ClientApp {

    public static void main(String[] args) {
        String serverAddress = "localhost"; // Cambia esto por la dirección del servidor
        int serverPort = 12345;

        try {
            try (Socket socket = new Socket(serverAddress, serverPort)) {
                DataOutputStream outputStream = new DataOutputStream(socket.getOutputStream());

                String message = "Hola, servidor. Este es un mensaje desde el cliente.";
                outputStream.writeUTF(message);
            }
        } catch (UnknownHostException e) {
            System.err.println("Host desconocido: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error de E/S: " + e.getMessage());
        }
    }
}
