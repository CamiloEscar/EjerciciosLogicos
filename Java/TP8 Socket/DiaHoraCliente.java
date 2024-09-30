
/**
 * @author camilo
 *
 * Ejercicio 3
 * Realice el ejemplo anterior, utilice una maquina Linux como Server donde consultar la hora.
 */
import java.net.Socket;
import java.io.IOException;
import java.io.DataInputStream;

public class DiaHoraCliente {

    public static void main(String[] args) {
        String host = "IP de linux"; // Reemplaza con la dirección IP de tu servidor Linux

        try {
            try (Socket socket = new Socket(host, 13)) {
                DataInputStream dataInput = new DataInputStream(socket.getInputStream());

                String line = dataInput.readLine();

                System.out.println("Conectado a: " + socket.getInetAddress());
                System.out.println("Puerto: " + socket.getPort());
                System.out.println("Día y hora: " + line);
            }
        } catch (IOException e) {
            System.err.println("Error al conectar al servidor: " + e.getMessage());
        }
    }
}
