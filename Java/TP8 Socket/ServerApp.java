
/**
 * @author camilo
 *
 * Ejercicio 7
 * Desarrollar una aplicación para enviar mensajes entre maquinas usando Sockets cliente y servidor
 */
import java.io.*;
import java.net.*;

public class ServerApp {

    public static void main(String[] args) {
        int port = 12345; // Puerto en el que el servidor estará escuchando

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Servidor escuchando en el puerto " + port);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado desde " + clientSocket.getInetAddress());

                DataInputStream inputStream = new DataInputStream(clientSocket.getInputStream());

                String message = inputStream.readUTF();
                System.out.println("Mensaje del cliente: " + message);

                clientSocket.close();
            }
        } catch (IOException e) {
            System.err.println("Error en el servidor: " + e.getMessage());
        }
    }
}
